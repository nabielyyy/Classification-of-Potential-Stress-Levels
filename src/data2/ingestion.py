import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def split_batch(df, batch_size=1000):
    for i in range(0, len(df), batch_size):
        yield df[i:i+batch_size], i//batch_size + 1

def save_batch(df, batch_num):
    os.makedirs("data/raw_batch", exist_ok=True)
    file_name = f"data/raw_batch/batch_{batch_num:03d}_raw.csv"
    df.to_csv(file_name, index=False)
    print(f"Saved {file_name}")

if __name__ == "__main__":
    df = load_data("data/raw/Smartphone_Usage_Productivity_Dataset_50000.csv")

    for batch, num in split_batch(df):
        save_batch(batch, num)
