import json
from src.utils import load_model
from src.config import MODEL_PATH
import pandas as pd

model = load_model(MODEL_PATH)

def lambda_handler(event, context):
    data = json.loads(event['body'])
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": int(prediction)})
    }
