from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import numpy as np
import joblib
from typing import List
import uvicorn
import os

app = FastAPI(title="ML Model API")

# 모델과 스케일러 파일 경로 확인
MODEL_PATH = 'model/model.pkl'
SCALER_PATH = 'data/scaler.pkl'

# 필요한 특성 컬럼 정의
FEATURE_COLUMNS = ['session_duration', 'page_views', 'clicks', 'scroll_depth', 'time_on_site']

# 파일 존재 여부 확인
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"Scaler file not found at {SCALER_PATH}")

# 모델과 스케일러 로드
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    raise Exception(f"Error loading model or scaler: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "ML Model API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # CSV 파일 읽기
        df = pd.read_csv(file.file)
        
        # 필요한 컬럼 확인
        if not all(col in df.columns for col in FEATURE_COLUMNS):
            raise HTTPException(
                status_code=400, 
                detail=f"CSV file must contain columns: {FEATURE_COLUMNS}"
            )
        
        # 필요한 컬럼만 선택
        X = df[FEATURE_COLUMNS]
        
        # 스케일링
        scaled_data = scaler.transform(X)
        
        # 예측 및 확률 계산
        predictions = model.predict(scaled_data)
        probabilities = model.predict_proba(scaled_data)
        
        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_batch")
async def predict_batch(data: List[dict]):
    try:
        # 데이터프레임으로 변환
        df = pd.DataFrame(data)
        
        # 필요한 컬럼 확인
        if not all(col in df.columns for col in FEATURE_COLUMNS):
            raise HTTPException(
                status_code=400, 
                detail=f"Input data must contain columns: {FEATURE_COLUMNS}"
            )
        
        # 필요한 컬럼만 선택
        X = df[FEATURE_COLUMNS]
        
        # 스케일링
        scaled_data = scaler.transform(X)
        
        # 예측 및 확률 계산
        predictions = model.predict(scaled_data)
        probabilities = model.predict_proba(scaled_data)
        
        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 