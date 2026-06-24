import pandas as pd

fund = pd.read_csv("data/fund_master.csv")

print("Fund Houses")
print(fund["fund_house"].unique())

print("\nCategories")
print(fund["category"].unique())

print("\nSub Categories")
print(fund["subcategory"].unique())

print("\nRisk Grades")
print(fund["risk_grade"].unique())