from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from src.utils import load_model, load_data, split_data
from src.config import MODEL_PATH, PROCESSED_DATA_PATH

def evaluate():
    model = load_model(MODEL_PATH)
    df = load_data(PROCESSED_DATA_PATH)
    X_train, X_test, y_train, y_test = split_data(df)
    
    y_pred = model.predict(X_test)
    
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("F1-score:", f1_score(y_test, y_pred))
    print("Matriz de confusão:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate()
