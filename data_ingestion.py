-- =====================================
-- Mutual Fund Analytics Database Schema
-- =====================================

DROP TABLE IF EXISTS fund_master;
DROP TABLE IF EXISTS nav_history;
DROP TABLE IF EXISTS fund_returns;
DROP TABLE IF EXISTS aum_data;
DROP TABLE IF EXISTS investor_transactions;
DROP TABLE IF EXISTS expense_ratios;
DROP TABLE IF EXISTS risk_metrics;
DROP TABLE IF EXISTS scheme_categories;
DROP TABLE IF EXISTS benchmark_returns;
DROP TABLE IF EXISTS fund_manager_details;

---------------------------------------------------

CREATE TABLE fund_master(
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    subcategory TEXT,
    risk_grade TEXT
);

---------------------------------------------------

CREATE TABLE nav_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    date DATE,
    nav REAL,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE fund_returns(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE aum_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    aum REAL,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE investor_transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    date DATE,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE expense_ratios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    expense_ratio REAL,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE risk_metrics(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    beta REAL,
    alpha REAL,
    sharpe REAL,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE scheme_categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    category TEXT,
    subcategory TEXT,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);

---------------------------------------------------

CREATE TABLE benchmark_returns(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    benchmark_name TEXT,
    returns REAL
);

---------------------------------------------------

CREATE TABLE fund_manager_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    manager_name TEXT,
    experience INTEGER,
    FOREIGN KEY (scheme_code)
        REFERENCES fund_master(scheme_code)
);