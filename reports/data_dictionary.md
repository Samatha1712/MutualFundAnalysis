# Mutual Fund Analytics Platform

# Data Dictionary

---

## 1. fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | Unique AMFI Scheme Code |
| scheme_name | Text | Name of Mutual Fund Scheme |
| fund_house | Text | Mutual Fund Company |
| category | Text | Equity/Debt Category |
| subcategory | Text | Fund Classification |
| risk_grade | Text | Risk Level |

---

## 2. nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 3. fund_returns.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| return_1y | Float | One Year Return |
| return_3y | Float | Three Year Return |
| return_5y | Float | Five Year Return |

---

## 4. aum_data.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| aum | Float | Assets Under Management |

---

## 5. expense_ratios.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| expense_ratio | Float | Expense Ratio Percentage |

---

## 6. investor_transactions.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | Integer | Transaction ID |
| scheme_code | Integer | AMFI Scheme Code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount | Float | Investment Amount |
| date | Date | Transaction Date |

---

## 7. risk_metrics.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| beta | Float | Beta Value |
| alpha | Float | Alpha Value |
| sharpe | Float | Sharpe Ratio |

---

## 8. scheme_categories.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| category | Text | Mutual Fund Category |
| subcategory | Text | Mutual Fund Subcategory |

---

## 9. benchmark_returns.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| benchmark_name | Text | Benchmark Index |
| returns | Float | Benchmark Return |

---

## 10. fund_manager_details.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| manager_name | Text | Fund Manager |
| experience | Integer | Years of Experience |

---

# Project Summary

This database contains cleaned mutual fund datasets used for analysis, visualization, and SQL reporting. All datasets were cleaned, validated, and loaded into SQLite as part of the Day 2 ETL process.