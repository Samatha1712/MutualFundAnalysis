import os
import pandas as pd

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

print("="*60)
print("DATA CLEANING STARTED")
print("="*60)

for file in os.listdir(RAW_FOLDER):

    if file.endswith(".csv"):

        print(f"\nProcessing {file}")

        path = os.path.join(RAW_FOLDER,file)

        df = pd.read_csv(path)

        print("Original Shape:",df.shape)

        df = df.drop_duplicates()

        for column in df.columns:

            if df[column].dtype=="object":

                df[column]=df[column].fillna("Unknown")

            else:

                df[column]=df[column].fillna(0)

        if "date" in df.columns:

            df["date"]=pd.to_datetime(
                df["date"],
                errors="coerce"
            )

        if "nav" in df.columns:

            df=df[df["nav"]>0]

        if "amount" in df.columns:

            df=df[df["amount"]>0]

        save_path=os.path.join(PROCESSED_FOLDER,file)

        df.to_csv(save_path,index=False)

        print("Saved:",save_path)

print("\nCleaning Completed Successfully")