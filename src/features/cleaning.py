import pandas as pd

def clean_data(df):
    # 1. Missing value → isi mean
    df = df.fillna(df.mean(numeric_only=True))

    # 2. Validasi range
    df = df[df["Sleep_Hours"] >= 0]
    df = df[df["Daily_Phone_Hours"] <= 24]

    # 3. Hapus duplikat
    df = df.drop_duplicates()

    return df
