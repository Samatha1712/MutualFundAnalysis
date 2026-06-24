import pandas as pd
import os

folder = "data"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder,file)

        print("\n"+"="*60)

        print("FILE:",file)

        df = pd.read_csv(path)

        print("Shape")
        print(df.shape)

        print("Data Types")
        print(df.dtypes)

        print("Head")
        print(df.head())

        print("Missing Values")
        print(df.isnull().sum())