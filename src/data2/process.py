import pandas as pd
import os
from src.features.cleaning import clean_data
from src.features.feature_engineering import encode_features

def process_batch(file_path, batch_num):
    df = pd.read_csv(file_path)

    df = clean_data(df)
    df = encode_features(df)

    os.makedirs("data/processed", exist_ok=True)
    output_path = f"data/processed/batch_{batch_num:03d}_processed.csv"

    df.to_csv(output_path, index=False)
    print(f"Processed saved: {output_path}")

if __name__ == "__main__":
    folder = "data/raw_batch"

    for file in os.listdir(folder):
        batch_num = int(file.split("_")[1])
        process_batch(os.path.join(folder, file), batch_num)
