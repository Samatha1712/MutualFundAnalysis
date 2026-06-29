import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("="*60)
print("Mutual Fund Analytics - EDA")
print("="*60)

# --------------------------------------------------
# Folder
# --------------------------------------------------

FIGURES = "reports/figures"

os.makedirs(FIGURES, exist_ok=True)

# --------------------------------------------------
# Load Processed Datasets
# --------------------------------------------------

print("\nLoading datasets...\n")

fund_master = pd.read_csv("data/processed/fund_master.csv")

fund_returns = pd.read_csv("data/processed/fund_returns.csv")

expense = pd.read_csv("data/processed/expense_ratios.csv")

aum = pd.read_csv("data/processed/aum_data.csv")

risk = pd.read_csv("data/processed/risk_metrics.csv")

nav = pd.read_csv("data/processed/nav_history.csv")

scheme = pd.read_csv("data/processed/scheme_categories.csv")

transactions = pd.read_csv("data/processed/investor_transactions.csv")

manager = pd.read_csv("data/processed/fund_manager_details.csv")

codes = pd.read_csv("data/processed/amfi_codes.csv")

print("✓ All datasets loaded successfully.")

# --------------------------------------------------
# Load Supplementary Data
# --------------------------------------------------

age = pd.read_csv("data/supplementary/investor_demographics.csv")

gender = pd.read_csv("data/supplementary/gender_distribution.csv")

state = pd.read_csv("data/supplementary/state_distribution.csv")

sector = pd.read_csv("data/supplementary/sector_allocation.csv")

sip = pd.read_csv("data/supplementary/sip_monthly.csv")

print("✓ Supplementary datasets loaded.")

# --------------------------------------------------
# Convert Dates
# --------------------------------------------------

if "date" in nav.columns:
    nav["date"] = pd.to_datetime(nav["date"])

# --------------------------------------------------
# Summary Statistics
# --------------------------------------------------

print("\nSUMMARY")

print("="*50)

print("\nFund Houses")

print(fund_master["fund_house"].value_counts())

print("\nCategories")

print(fund_master["category"].value_counts())

print("\nRisk Grades")

print(fund_master["risk_grade"].value_counts())

print("\nExpense Ratio")

print(expense.describe())

print("\nAUM")

print(aum.describe())

print("\nNAV")

print(nav.describe())

print("\nSummary completed successfully.")

print("="*50)

#############################################################
# CHART 1 - Fund House Distribution
#############################################################

print("\nCreating Chart 1...")

plt.figure(figsize=(8,5))

fund_master["fund_house"].value_counts().plot(
    kind="bar",
    color="skyblue"
)

plt.title("Fund House Distribution")
plt.xlabel("Fund House")
plt.ylabel("Number of Schemes")

plt.tight_layout()

plt.savefig("reports/figures/chart1_fund_house.png")

plt.close()

print("Chart 1 Saved")


#############################################################
# CHART 2 - Risk Grade Distribution
#############################################################

print("\nCreating Chart 2...")

plt.figure(figsize=(6,5))

sns.countplot(data=fund_master,x="risk_grade")

plt.title("Risk Grade Distribution")

plt.tight_layout()

plt.savefig("reports/figures/chart2_risk_grade.png")

plt.close()

print("Chart 2 Saved")


#############################################################
# CHART 3 - Category Distribution
#############################################################

print("\nCreating Chart 3...")

plt.figure(figsize=(7,5))

sns.countplot(data=fund_master,x="category")

plt.title("Fund Categories")

plt.tight_layout()

plt.savefig("reports/figures/chart3_category.png")

plt.close()

print("Chart 3 Saved")


#############################################################
# CHART 4 - Expense Ratio Histogram
#############################################################

print("\nCreating Chart 4...")

plt.figure(figsize=(7,5))

plt.hist(expense["expense_ratio"],bins=10)

plt.title("Expense Ratio Distribution")

plt.xlabel("Expense Ratio")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("reports/figures/chart4_expense_ratio.png")

plt.close()

print("Chart 4 Saved")


#############################################################
# CHART 5 - AUM Comparison
#############################################################

merged = pd.merge(
    aum,
    fund_master[["scheme_code", "scheme_name"]],
    on="scheme_code"
)

plt.figure(figsize=(9,5))

plt.bar(
    merged["scheme_name"],
    merged["aum"]
)

plt.xticks(rotation=45)

plt.title("Assets Under Management")

plt.ylabel("AUM")

plt.tight_layout()

plt.savefig("reports/figures/chart5_aum.png")

plt.close()

print("Chart 5 Saved")

print("\nFirst Five Charts Completed Successfully")



#############################################################
# CHART 6 - NAV Trend
#############################################################

print("\nCreating Chart 6...")

nav["date"] = pd.to_datetime(nav["date"])

plt.figure(figsize=(10,5))

for code in nav["scheme_code"].unique():
    temp = nav[nav["scheme_code"] == code]
    plt.plot(temp["date"], temp["nav"], marker="o", label=str(code))

plt.title("NAV Trend")

plt.xlabel("Date")

plt.ylabel("NAV")

plt.legend(title="Scheme Code")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/figures/chart6_nav_trend.png")

plt.close()

print("Chart 6 Saved")

#############################################################
# CHART 7 - SIP Trend
#############################################################

print("\nCreating Chart 7...")

plt.figure(figsize=(8,5))

plt.plot(
    sip["Month"],
    sip["SIP"],
    marker="o",
    linewidth=2
)

plt.title("Monthly SIP Trend")

plt.xlabel("Month")

plt.ylabel("SIP")

plt.grid(True)

plt.tight_layout()

plt.savefig("reports/figures/chart7_sip_trend.png")

plt.close()

print("Chart 7 Saved")

#############################################################
# CHART 8 - Category Heatmap
#############################################################

print("\nCreating Chart 8...")

heat = pd.crosstab(
    fund_master["category"],
    fund_master["risk_grade"]
)

plt.figure(figsize=(6,4))

sns.heatmap(
    heat,
    annot=True,
    cmap="Blues"
)

plt.title("Category vs Risk Grade")

plt.tight_layout()

plt.savefig("reports/figures/chart8_heatmap.png")

plt.close()

print("Chart 8 Saved")

#############################################################
# CHART 9 - Investor Age
#############################################################

print("\nCreating Chart 9...")

plt.figure(figsize=(6,6))

plt.pie(
    age["Investors"],
    labels=age["Age_Group"],
    autopct="%1.1f%%"
)

plt.title("Investor Age Distribution")

plt.savefig("reports/figures/chart9_age_distribution.png")

plt.close()

print("Chart 9 Saved")

#############################################################
# CHART 10 - Gender Distribution
#############################################################

print("\nCreating Chart 10...")

plt.figure(figsize=(6,6))

plt.pie(
    gender["Count"],
    labels=gender["Gender"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.tight_layout()

plt.savefig("reports/figures/chart10_gender_distribution.png")

plt.close()

print("Chart 10 Saved")

#############################################################
# CHART 11 - State Distribution
#############################################################

print("\nCreating Chart 11...")

plt.figure(figsize=(8,5))

plt.barh(
    state["State"],
    state["Investors"]
)

plt.barh(
    state["State"],
    state["Investors"]
)

plt.title("State-wise Investor Distribution")
plt.xlabel("Number of Investors")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("reports/figures/chart11_state_distribution.png")

print("Chart 11 Saved")

plt.close()

#############################################################
# CHART 12 - T30 vs B30
#############################################################

print("\nCreating Chart 12...")

t30 = state["Investors"][:3].sum()
b30 = state["Investors"][3:].sum()

plt.figure(figsize=(6,6))

plt.pie(
    [t30, b30],
    labels=["T30", "B30"],
    autopct="%1.1f%%"
)

plt.title("T30 vs B30")

plt.savefig("reports/figures/chart12_t30_b30.png")

plt.close()

print("Chart 12 Saved")

#############################################################
# CHART 13 - Fund Returns
#############################################################

print("\nCreating Chart 13...")

returns = fund_returns.set_index("scheme_code")

returns.plot(kind="bar", figsize=(10,5))

plt.title("Fund Returns")

plt.ylabel("Return (%)")

plt.tight_layout()

plt.savefig("reports/figures/chart13_returns.png")

plt.close()

print("Chart 13 Saved")

#############################################################
# CHART 14 - Correlation Matrix
#############################################################

print("\nCreating Chart 14...")

corr = fund_returns.drop(columns=["scheme_code"]).corr()

plt.figure(figsize=(6,5))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Return Correlation Matrix")

plt.tight_layout()

plt.savefig("reports/figures/chart14_correlation.png")

plt.close()

print("Chart 14 Saved")

#############################################################
# CHART 15 - Sector Allocation
#############################################################

print("\nCreating Chart 15...")

plt.figure(figsize=(7,7))

plt.pie(
    sector["Allocation"],
    labels=sector["Sector"],
    autopct="%1.1f%%"
)

centre = plt.Circle((0,0),0.60,fc="white")

plt.gca().add_artist(centre)

plt.title("Sector Allocation")

plt.savefig("reports/figures/chart15_sector_allocation.png")

plt.close()

print("Chart 15 Saved")

print("\nAll 15 Charts Generated Successfully!")

