CREATE TABLE fund_master(
scheme_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
subcategory TEXT,
risk_grade TEXT
);

CREATE TABLE nav_history(
scheme_code INTEGER,
date DATE,
nav REAL
);

CREATE TABLE fund_returns(
scheme_code INTEGER,
return_1y REAL,
return_3y REAL,
return_5y REAL
);

CREATE TABLE aum_data(
scheme_code INTEGER,
aum REAL
);

CREATE TABLE investor_transactions(
transaction_id INTEGER PRIMARY KEY,
scheme_code INTEGER,
amount REAL,
transaction_type TEXT,
date DATE
);

CREATE TABLE expense_ratios(
scheme_code INTEGER,
expense_ratio REAL
);

CREATE TABLE risk_metrics(
scheme_code INTEGER,
beta REAL,
alpha REAL,
sharpe REAL
);

CREATE TABLE scheme_categories(
scheme_code INTEGER,
category TEXT
);

CREATE TABLE benchmark_returns(
benchmark TEXT,
returns REAL
);

CREATE TABLE fund_manager_details(
manager_name TEXT,
scheme_code INTEGER
);