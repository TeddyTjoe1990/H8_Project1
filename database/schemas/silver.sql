-- ============================================================================
-- MILESTONE 1 - LANGKAH 3: SILVER LAYER & REJECTED RECORDS (silver.sql)
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS silver;
SET search_path TO silver;

DROP TABLE IF EXISTS silver_customers;
DROP TABLE IF EXISTS silver_transactions;
DROP TABLE IF EXISTS rejected_records;

-- 1. Tabel untuk menampung baris data yang gagal validasi (Data Quality Error)
CREATE TABLE rejected_records (
    rejection_id SERIAL PRIMARY KEY,
    run_id INT,
    source_table VARCHAR(100) NOT NULL,
    record_data JSONB NOT NULL,       -- Menyimpan seluruh kolom baris yang gagal dalam format JSON
    error_reason TEXT NOT NULL,       -- Keterangan kenapa data ditolak
    rejected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabel Clean Customers
CREATE TABLE silver_customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    signup_date DATE,
    country VARCHAR(50),
    email VARCHAR(150),
    transformed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tabel Clean Transactions
CREATE TABLE silver_transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    customer_id INT REFERENCES silver_customers(customer_id),
    product_id VARCHAR(50),
    quantity INT CHECK (quantity > 0),
    price NUMERIC(12, 2) CHECK (price >= 0),
    total_amount NUMERIC(12, 2),
    transaction_date TIMESTAMP,
    transformed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);