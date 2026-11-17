-- ============================================================================
-- MILESTONE 1 - LANGKAH 2: BRONZE LAYER (bronze.sql)
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS bronze;
SET search_path TO bronze;

DROP TABLE IF EXISTS raw_customers;
DROP TABLE IF EXISTS raw_transactions;

-- Tabel Raw Customers
CREATE TABLE raw_customers (
    customer_id TEXT,
    customer_name TEXT,
    signup_date TEXT,
    country TEXT,
    email TEXT,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabel Raw Transactions
CREATE TABLE raw_transactions (
    transaction_id TEXT,
    customer_id TEXT,
    product_id TEXT,
    quantity TEXT,
    price TEXT,
    transaction_date TEXT,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);