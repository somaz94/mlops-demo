from fastapi import FastAPI, File, UploadFile
import pandas as pd
import numpy as np
import joblib
from typing import List
import uvicorn

app = FastAPI(title="ML Model API")

# 모델과 스케일러 로드
model = joblib.load('model/model.pkl')
scaler = joblib.load('data/scaler.pkl')

@app.get("/")
def read_root():
    return {"message": "ML Model API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # CSV 파일 읽기
    df = pd.read_csv(file.file)
    
    # 스케일링
    scaled_data = scaler.transform(df)
    
    # 예측
    predictions = model.predict(scaled_data)
    
    return {"predictions": predictions.tolist()}

@app.post("/predict_batch")
async def predict_batch(data: List[dict]):
    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    
    # 스케일링
    scaled_data = scaler.transform(df)
    
    # 예측
    predictions = model.predict(scaled_data)
    
    return {"predictions": predictions.tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 