FROM python:3.13-slim

WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 데이터 전처리 및 모델 학습 실행
RUN python preprocess.py && python train_model.py

EXPOSE 8000

CMD ["python", "predict_api.py"] 