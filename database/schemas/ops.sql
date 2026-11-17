-- ====================================================================
-- MILESTONE 1 - STEP 1: OPS LAYER (OPERATIONAL & PIPELINE METADATA)
-- ====================================================================

-- Membuat Schema ops jika belum ada
CREATE SCHEMA IF NOT EXISTS ops;

-- --------------------------------------------------------------------
-- 1. Tabel ops.pipeline_runs
-- Mencatat setiap eksekusi pipeline (waktu mulai, selesai, status, error)
-- --------------------------------------------------------------------
DROP TABLE IF EXISTS ops.pipeline_runs CASCADE;
CREATE TABLE ops.pipeline_runs (
    run_id SERIAL PRIMARY KEY,
    pipeline_name VARCHAR(100) NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('RUNNING', 'SUCCESS', 'FAILED')),
    error_message TEXT
);

-- --------------------------------------------------------------------
-- 2. Tabel ops.ingested_files
-- Mencatat nama file yang di-ingest beserta jumlah record-nya
-- --------------------------------------------------------------------
DROP TABLE IF EXISTS ops.ingested_files CASCADE;
CREATE TABLE ops.ingested_files (
    file_id SERIAL PRIMARY KEY,
    run_id INT REFERENCES ops.pipeline_runs(run_id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    record_count INT NOT NULL DEFAULT 0,
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- --------------------------------------------------------------------
-- 3. Tabel ops.quality_results
-- Mencatat hasil pengujian kualitas data (Data Quality Audit)
-- --------------------------------------------------------------------
DROP TABLE IF EXISTS ops.quality_results CASCADE;
CREATE TABLE ops.quality_results (
    check_id SERIAL PRIMARY KEY,
    run_id INT REFERENCES ops.pipeline_runs(run_id) ON DELETE CASCADE,
    check_name VARCHAR(150) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('PASSED', 'FAILED', 'WARNING')),
    actual_value NUMERIC,
    target_value NUMERIC,
    checked_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- --------------------------------------------------------------------
-- Contoh Pengisian Data (Dummy Records untuk Testing)
-- --------------------------------------------------------------------
INSERT INTO ops.pipeline_runs (pipeline_name, started_at, ended_at, status, error_message)
VALUES ('m1_etl_pipeline', CURRENT_TIMESTAMP - INTERVAL '5 minutes', CURRENT_TIMESTAMP, 'SUCCESS', NULL);

INSERT INTO ops.ingested_files (run_id, file_name, record_count)
VALUES 
(1, 'raw_customers.csv', 1000),
(1, 'raw_orders.csv', 5000);

INSERT INTO ops.quality_results (run_id, check_name, status, actual_value, target_value)
VALUES 
(1, 'null_check_customer_id', 'PASSED', 0, 0),
(1, 'row_count_check_orders', 'PASSED', 5000, 5000);