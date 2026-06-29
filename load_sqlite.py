import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

folder = "data/processed"

print("="*60)
print("LOADING DATA INTO SQLITE")
print("="*60)

for file in os.listdir(folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv","")

        path = os.path.join(folder,file)

        df = pd.read_csv(path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded ({len(df)} rows)")

print("\nDatabase Created Successfully")