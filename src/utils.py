import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def save_data(df, path):
    df.to_csv(path, index=False)

def split_data(df, target='delayed'):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)
