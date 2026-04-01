import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_all_data():
    folder = "data/processed"
    all_df = []

    for file in os.listdir(folder):
        df = pd.read_csv(os.path.join(folder, file))
        all_df.append(df)

    return pd.concat(all_df, ignore_index=True)

def train_model():
    df = load_all_data()

    # target (misal: Stress_Level)
    X = df.drop("Stress_Level", axis=1)
    y = df["Stress_Level"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Logistic Regression
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)

    # Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    # Evaluasi
    pred_lr = lr.predict(X_test)
    pred_rf = rf.predict(X_test)

    print("Accuracy LR:", accuracy_score(y_test, pred_lr))
    print("Accuracy RF:", accuracy_score(y_test, pred_rf))

if __name__ == "__main__":
    train_model()
