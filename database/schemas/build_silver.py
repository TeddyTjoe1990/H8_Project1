import pandas as pd
import psycopg2
import json
from sqlalchemy import create_engine

DB_CONFIG = {
    "dbname": "ai_engineer_milestone1",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

def run_silver_pipeline():
    engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    pipeline_name = "silver_transformation_pipeline"
    
    try:
        # 1. Start Pipeline Run
        cursor.execute(
            "INSERT INTO ops.pipeline_runs (pipeline_name, status) VALUES (%s, 'RUNNING') RETURNING run_id;",
            (pipeline_name,)
        )
        run_id = cursor.fetchone()[0]
        conn.commit()
        print(f"[*] Silver Pipeline started with run_id: {run_id}")

        # --- A. PROSES TRANSFORMASI CUSTOMERS ---
        df_cust = pd.read_sql("SELECT * FROM bronze.raw_customers", engine)
        valid_customers = []
        
        for _, row in df_cust.iterrows():
            try:
                # Validasi sederhana: customer_id harus angka & email tidak boleh kosong/null
                if pd.isna(row['customer_id']) or not str(row['customer_id']).isdigit():
                    raise ValueError("Invalid or missing customer_id")
                if pd.isna(row['email']) or '@' not in str(row['email']):
                    raise ValueError("Invalid email format")
                
                valid_customers.append({
                    "customer_id": int(row['customer_id']),
                    "customer_name": str(row['customer_name']).strip().title(),
                    "signup_date": pd.to_datetime(row['signup_date'], errors='coerce'),
                    "country": str(row['country']).strip().upper(),
                    "email": str(row['email']).strip().lower()
                })
            except Exception as err:
                # Catat ke rejected_records jika gagal validasi
                cursor.execute(
                    """INSERT INTO silver.rejected_records (run_id, source_table, record_data, error_reason) 
                       VALUES (%s, %s, %s, %s);""",
                    (run_id, 'raw_customers', json.dumps(row.to_dict()), str(err))
                )
        
        conn.commit()
        
        if valid_customers:
            df_valid_cust = pd.DataFrame(valid_customers)
            df_valid_cust.to_sql('silver_customers', engine, schema='silver', if_exists='append', index=False)
            print(f"[+] Loaded {len(df_valid_cust)} valid records into silver.silver_customers")

        # --- B. PROSES TRANSFORMASI TRANSACTIONS ---
        df_tx = pd.read_sql("SELECT * FROM bronze.raw_transactions", engine)
        # Ambil daftar customer_id yang valid di silver agar foreign key terjaga
        valid_cust_ids = pd.read_sql("SELECT customer_id FROM silver.silver_customers", engine)['customer_id'].tolist()
        
        valid_transactions = []
        for _, row in df_tx.iterrows():
            try:
                if pd.isna(row['transaction_id']) or str(row['transaction_id']).strip() == "":
                    raise ValueError("Missing transaction_id")
                
                c_id = int(row['customer_id']) if not pd.isna(row['customer_id']) and str(row['customer_id']).isdigit() else None
                if c_id not in valid_cust_ids:
                    raise ValueError(f"Foreign key violation: customer_id {c_id} not found in silver_customers")
                
                qty = int(row['quantity']) if not pd.isna(row['quantity']) and str(row['quantity']).isdigit() else 0
                price = float(row['price']) if not pd.isna(row['price']) else 0.0
                
                if qty <= 0 or price < 0:
                    raise ValueError("Quantity must be > 0 and price >= 0")

                valid_transactions.append({
                    "transaction_id": str(row['transaction_id']).strip(),
                    "customer_id": c_id,
                    "product_id": str(row['product_id']).strip(),
                    "quantity": qty,
                    "price": price,
                    "total_amount": qty * price,
                    "transaction_date": pd.to_datetime(row['transaction_date'], errors='coerce')
                })
            except Exception as err:
                cursor.execute(
                    """INSERT INTO silver.rejected_records (run_id, source_table, record_data, error_reason) 
                       VALUES (%s, %s, %s, %s);""",
                    (run_id, 'raw_transactions', json.dumps(row.to_dict()), str(err))
                )
        
        conn.commit()
        
        if valid_transactions:
            df_valid_tx = pd.DataFrame(valid_transactions)
            df_valid_tx.to_sql('silver_transactions', engine, schema='silver', if_exists='append', index=False)
            print(f"[+] Loaded {len(df_valid_tx)} valid records into silver.silver_transactions")

        # Update status pipeline SUCCESS
        cursor.execute(
            "UPDATE ops.pipeline_runs SET finished_at = CURRENT_TIMESTAMP, status = 'SUCCESS' WHERE run_id = %s;",
            (run_id,)
        )
        conn.commit()
        print("[+] Silver Pipeline COMPLETED successfully.")

    except Exception as e:
        conn.rollback()
        print(f"[-] Silver Pipeline FAILED: {str(e)}")
        cursor.execute(
            "UPDATE ops.pipeline_runs SET finished_at = CURRENT_TIMESTAMP, status = 'FAILED', error_message = %s WHERE run_id = %s;",
            (str(e), run_id)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

if _name_ == "_main_":
    run_silver_pipeline()