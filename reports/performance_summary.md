# Fund Performance Analytics Summary

## Objective

This report summarizes the performance analysis of the Mutual Fund Analytics Platform.

---

## Datasets Used

- fund_master.csv
- fund_returns.csv
- nav_history.csv
- benchmark_returns.csv
- expense_ratios.csv
- risk_metrics.csv

---

## Performance Metrics Generated

### 1. Daily Returns
Calculated using:

Daily Return = (Today's NAV / Previous NAV) - 1

---

### 2. CAGR

Calculated for:

- 1 Year
- 3 Year
- 5 Year

Formula:

CAGR = (Ending NAV / Beginning NAV)^(1/n) - 1

---

### 3. Sharpe Ratio

Measures return per unit of total risk.

Higher Sharpe Ratio indicates better performance.

---

### 4. Sortino Ratio

Measures return considering downside risk only.

Useful for comparing funds with lower downside volatility.

---

### 5. Maximum Drawdown

Measures the largest decline from peak NAV.

Lower drawdown indicates more stable performance.

---

### 6. Alpha & Beta

Alpha measures excess return over benchmark.

Beta measures market sensitivity.

---

### Benchmark Comparison

Top performing funds were compared with benchmark returns using a line chart.

---

## Files Generated

- daily_returns.csv
- cagr.csv
- sharpe_ratio.csv
- sortino_ratio.csv
- maximum_drawdown.csv
- alpha_beta.csv

---

## Conclusion

The Mutual Fund Performance Analytics module successfully calculated all required financial performance metrics and generated benchmark comparison visualizations for further reporting.