import pandas as pd
from src.utils import save_data

def make_sample():
    data = {
        "flight": [1001, 1002, 1003, 1004],
        "airline": ["A", "B", "A", "C"],
        "scheduled_time": [8, 9, 10, 11],
        "weather": ["clear", "rain", "fog", "clear"],
        "delayed": [0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    save_data(df, "data/raw/flights.csv")

if __name__ == "__main__":
    make_sample()
