# Mutual Fund Analytics Data Dictionary

## fund_master.csv

| Column | Type | Description |
|----------|----------|-------------|
| scheme_code | Integer | AMFI Scheme Code |
| scheme_name | Text | Scheme Name |
| fund_house | Text | Fund House |
| category | Text | Fund Category |
| subcategory | Text | Fund Subcategory |
| risk_grade | Text | Risk Level |

---

## nav_history.csv

| Column | Type | Description |
|----------|----------|-------------|
| scheme_code | Integer | AMFI Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## fund_returns.csv

Stores annual returns.

---

## expense_ratios.csv

Stores expense ratio of each scheme.

---

## risk_metrics.csv

Contains Beta, Alpha and Sharpe Ratio.

---

## investor_transactions.csv

Contains investor transaction details.

---

## benchmark_returns.csv

Contains benchmark index returns.

---

## fund_manager_details.csv

Contains fund manager information.

---

## scheme_categories.csv

Contains mutual fund category information.

---

## aum_data.csv

Contains Assets Under Management.