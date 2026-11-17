import os
import pandas as pd
import psycopg2
from datetime import datetime

# Konfigurasi Koneksi Database (Sesuaikan dengan credential Anda)
DB_CONFIG = {
    "dbname": "ai_engineer_milestone1",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

def run_bronze_pipeline():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    pipeline_name = "bronze_ingestion_pipeline"
    
    try:
        # 1. Mulai Pipeline Run (Catat ke ops.pipeline_runs)
        cursor.execute(
            "INSERT INTO ops.pipeline_runs (pipeline_name, status) VALUES (%s, 'RUNNING') RETURNING run_id;",
            (pipeline_name,)
        )
        run_id = cursor.fetchone()[0]
        conn.commit()
        print(f"[*] Pipeline started with run_id: {run_id}")

        # Path file sumber (asumsi file CSV berada di folder data/)
        files_to_ingest = {
            "raw_customers": "data/customers.csv",
            "raw_transactions": "data/transactions.csv"
        }

        total_records = 0

        for table_name, file_path in files_to_ingest.items():
            if os.path.exists(file_path):
                df = pd.read_csv(file_path, dtype=str) # Baca semua sebagai string agar aman di Bronze
                record_count = len(df)
                
                # Masukkan data ke database secara bulk (atau menggunakan iterrows/to_sql)
                # Contoh sederhana menggunakan psycopg2 execute_values atau pandas to_sql
                from sqlalchemy import create_engine
                engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")
                
                df.to_sql(table_name, engine, schema='bronze', if_exists='append', index=False)
                
                # Catat file yang berhasil di-ingest ke ops.ingested_files
                cursor.execute(
                    "INSERT INTO ops.ingested_files (run_id, file_name, record_count) VALUES (%s, %s, %s);",
                    (run_id, file_path, record_count)
                )
                total_records += record_count
                print(f"[+] Successfully ingested {record_count} rows into bronze.{table_name}")
            else:
                raise FileNotFoundError(f"File source tidak ditemukan: {file_path}")

        # Update status pipeline menjadi SUCCESS
        cursor.execute(
            "UPDATE ops.pipeline_runs SET finished_at = CURRENT_TIMESTAMP, status = 'SUCCESS' WHERE run_id = %s;",
            (run_id,)
        )
        conn.commit()
        print("[+] Bronze Pipeline COMPLETED successfully.")

    except Exception as e:
        conn.rollback()
        print(f"[-] Pipeline FAILED: {str(e)}")
        cursor.execute(
            "UPDATE ops.pipeline_runs SET finished_at = CURRENT_TIMESTAMP, status = 'FAILED', error_message = %s WHERE run_id = %s;",
            (str(e), run_id)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

if _name_ == "_main_":
    run_bronze_pipeline()