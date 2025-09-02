from flask import Flask, request, jsonify
from src.utils import load_model
from src.config import MODEL_PATH
import pandas as pd

app = Flask(__name__)
model = load_model(MODEL_PATH)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
