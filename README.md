# MLOps Demo

간단한 머신러닝 파이프라인 데모 프로젝트입니다.

## 프로젝트 구조

```
mlops-demo/
├── data/
│   └── user_activity.csv       # 원본 CSV 데이터
│   └── X.csv / y.csv          # 전처리된 입력/정답
├── model/
│   └── model.pkl              # 학습된 모델
├── preprocess.py              # 전처리 스크립트
├── train_model.py             # 학습 및 저장
├── predict_api.py             # FastAPI 기반 추론 서버
├── requirements.txt           # 의존성 패키지
└── Dockerfile                 # Docker 설정
```

## 설치 및 실행

### 1. 로컬 환경에서 실행

1. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 의존성 설치:
```bash
pip install -r requirements.txt
```

3. 데이터 전처리:
```bash
python preprocess.py
```

4. 모델 학습:
```bash
python train_model.py
```

5. API 서버 실행:
```bash
python predict_api.py
```

### 2. Docker로 실행

1. Docker 이미지 빌드:
```bash
docker build -t mlops-demo .
```

2. Docker 컨테이너 실행:
```bash
docker run -p 8000:8000 mlops-demo
```

## API 사용법

1. 단일 예측 (CSV 파일):
```bash
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@data/test.csv"
```

2. 배치 예측 (JSON):
```bash
curl -X POST "http://localhost:8000/predict_batch" -H "accept: application/json" -H "Content-Type: application/json" -d '[{"feature1": 1.0, "feature2": 2.0}]'
```

## API 문서

FastAPI 자동 생성 문서는 다음 URL에서 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 