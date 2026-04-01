import pandas as pd

def encode_features(df):
    # contoh encoding kategorikal
    categorical_cols = df.select_dtypes(include=["object"]).columns

    df = pd.get_dummies(df, columns=categorical_cols)

    return df
