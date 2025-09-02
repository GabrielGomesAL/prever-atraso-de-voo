from sklearn.ensemble import RandomForestClassifier
from src.utils import split_data, save_model, load_data
from src.config import PROCESSED_DATA_PATH, MODEL_PATH

def train_model():
    df = load_data(PROCESSED_DATA_PATH)
    X_train, X_test, y_train, y_test = split_data(df)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    save_model(model, MODEL_PATH)
    print(f"Modelo treinado e salvo em {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
