# MLOps Demo

간단한 머신러닝 파이프라인 데모 프로젝트입니다.

<br/>

## 프로젝트 구조

```
mlops-demo/
├── data/
│   └── user_activity.csv       # 원본 CSV 데이터
│   └── X.csv / y.csv          # 전처리된 입력/정답
│   └── scaler.pkl             # 데이터 스케일링을 위한 StandardScaler 객체
├── model/
│   └── model.pkl              # 학습된 RandomForestClassifier 모델
├── preprocess.py              # 전처리 스크립트
├── train_model.py             # 학습 및 저장
├── predict_api.py             # FastAPI 기반 추론 서버
├── requirements.txt           # 의존성 패키지
└── Dockerfile                 # Docker 설정
```

<br/>

## 파일 설명

### model.pkl
- RandomForestClassifier 모델이 저장된 파일
- n_estimators=100, random_state=42로 설정
- joblib.dump()를 사용하여 저장
- 실제 사용시에는 train_model.py 실행으로 생성

### scaler.pkl
- StandardScaler 객체가 저장된 파일
- 데이터 전처리 시 사용되는 스케일링 파라미터 저장
- joblib.dump()를 사용하여 저장
- 실제 사용시에는 preprocess.py 실행으로 생성

<br/>

## 설치 및 실행

### 1. 로컬 환경에서 실행

1. 가상환경 생성 및 활성화:
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
결과: `(venv)` 프롬프트가 표시되며 가상환경이 활성화됩니다.

2. 의존성 설치:
```bash
pip3 install -r requirements.txt
```
결과: 필요한 패키지들이 설치되며, 설치 진행 상황이 표시됩니다.
```
Collecting numpy>=1.26.0
Collecting pandas>=2.1.0
Collecting scikit-learn>=1.3.2
...
Successfully installed numpy-1.26.0 pandas-2.1.0 scikit-learn-1.3.2 ...
```

3. 데이터 전처리:
```bash
python3 preprocess.py
```
결과: 데이터 전처리가 완료되며 다음 파일들이 생성됩니다.
```
data/X.csv  # 전처리된 입력 데이터
data/y.csv  # 전처리된 타겟 데이터
data/scaler.pkl  # 스케일링 파라미터
```

4. 모델 학습:
```bash
python3 train_model.py
```
결과: 모델 학습이 완료되며 다음 파일이 생성됩니다.
```
model/model.pkl  # 학습된 모델
```
학습 결과가 출력됩니다:
```
Model Accuracy: 0.XX
Model saved to model/model.pkl
```

5. API 서버 실행:
```bash
python3 predict_api.py
```
결과: FastAPI 서버가 시작되며 다음 메시지가 표시됩니다.
```
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

6. 가상환경 비활성화:
```bash
deactivate
```
결과: `(venv)` 프롬프트가 사라지며 가상환경이 비활성화됩니다.

<br/>

### 2. Docker로 실행

1. Docker 이미지 빌드:
```bash
docker build -t mlops-demo .
```
결과: Docker 이미지가 빌드되며 다음 메시지가 표시됩니다.
```
Sending build context to Docker daemon  XX.XXMB
Step 1/4 : FROM python:3.13-slim
...
Step 5/7 : RUN python preprocess.py && python train_model.py
전처리 완료:
- 학습 데이터: XX 샘플
- 테스트 데이터: XX 샘플
- 특성: ['session_duration', 'page_views', 'clicks', 'scroll_depth', 'time_on_site']
Model Accuracy: 0.XX
Model saved to model/model.pkl
...
Successfully built xxxxxxxxxxxx
Successfully tagged mlops-demo:latest
```

2. Docker 컨테이너 실행:
```bash
docker run -p 8000:8000 mlops-demo
```
결과: Docker 컨테이너가 시작되며 FastAPI 서버가 실행됩니다.
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**참고**: Docker 빌드 시점에 자동으로 데이터 전처리와 모델 학습이 실행되므로, 별도로 `preprocess.py`와 `train_model.py`를 실행할 필요가 없습니다.

<br/>

### 3. MLflow 실험 추적 및 UI 실행

1. MLflow 실험 자동 추적 예제 실행:
```bash
python3 mlflow_test.py
```
- Scikit-Learn 실험이 자동으로 추적되며, 결과는 `mlruns/` 폴더에 저장됩니다.

2. MLflow UI 실행:
```bash
mlflow ui
```
- 브라우저에서 [http://localhost:5000](http://localhost:5000) 접속 후 실험 결과를 시각적으로 확인할 수 있습니다.

**실무 팁**
- requirements.txt에 `mlflow`가 포함되어 있어야 합니다.
- `.gitignore`에 `mlruns/`를 추가해 실험 로그가 git에 포함되지 않도록 관리하세요.
- Docker 환경에서는 포트 매핑(`-p 5050:5050`)을 통해 외부에서 UI 접근이 가능합니다.

**예제 파일**: `mlflow_test.py`

<br/>

#### Docker에서 예측 API와 MLflow UI를 mlruns 폴더로 연동

1. 예측 API 서버용 이미지 빌드:
```bash
docker build -f Dockerfile.predictapi -t mlops-predictapi .
```
2. MLflow UI용 이미지 빌드:
```bash
docker build -f Dockerfile.mlflowui -t mlops-mlflowui .
``` 

3. 예측 API 서버 컨테이너 실행(mlruns 공유):
```bash
docker run -p 8000:8000 -v $(pwd)/mlruns:/app/mlruns mlops-predictapi
```
4. MLflow UI 컨테이너 실행(mlruns 공유):
```bash
docker run -p 5050:5050 -v $(pwd)/mlruns:/app/mlruns mlops-mlflowui
```
5. 브라우저에서 [http://localhost:5050](http://localhost:5050) 접속

- 두 컨테이너가 같은 mlruns 폴더를 공유하면, 예측 API에서 생성된 MLflow run도 UI에서 바로 확인할 수 있습니다.

<br/>

## API 사용법

<br/>

### 1. 단일 예측 (CSV 파일)
```bash
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@data/test.csv"
```
결과: JSON 형식의 예측 결과가 반환됩니다.
```json
{
  "predictions": [0, 1, 0],
  "probabilities": [0.2, 0.8, 0.3]
}
```

**참고**: Docker 사용 시 test.csv 파일을 먼저 생성하세요:
```bash
# 테스트 데이터 파일 생성
echo "session_duration,page_views,clicks,scroll_depth,time_on_site
130,6,9,80,190
50,2,3,35,65
170,7,11,85,210" > test.csv

# 파일 사용
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@test.csv"
```

**중요**: test.csv가 data/ 폴더에 있는 경우 다음 중 하나를 선택하세요:
1. data 디렉토리로 이동 후 실행:
```bash
cd data/
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@test.csv"
```

2. 또는 프로젝트 루트에서 전체 경로 사용:
```bash
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@data/test.csv"
```

<br/>

### 2. 배치 예측 (JSON)
```bash
curl -X POST "http://localhost:8000/predict_batch" -H "accept: application/json" -H "Content-Type: application/json" -d '[{"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190}]'
```
결과: JSON 형식의 예측 결과가 반환됩니다.
```json
{
  "predictions": [1],
  "probabilities": [0.75]
}
```

<br/>

### 3. Python requests 라이브러리 사용
```python
import requests
import pandas as pd

# CSV 파일로 예측
with open('test.csv', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/predict', files=files)
    print(response.json())

# JSON 데이터로 예측
data = [{"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190}]
response = requests.post('http://localhost:8000/predict_batch', json=data)
print(response.json())
```

**예제 파일**: `examples/python_example.py`

<br/>

### 4. JavaScript/Fetch API 사용
```javascript
// CSV 파일로 예측
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://localhost:8000/predict', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));

// JSON 데이터로 예측
const data = [{"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190}];

fetch('http://localhost:8000/predict_batch', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data));
```

**예제 파일**: `examples/web_example.html`, `examples/web_example.js`

<br/>

### 5. Postman 사용
1. **CSV 파일 예측**:
   - Method: POST
   - URL: `http://localhost:8000/predict`
   - Body: form-data
   - Key: `file` (File type)
   - Value: test.csv 파일 선택

2. **JSON 예측**:
   - Method: POST
   - URL: `http://localhost:8000/predict_batch`
   - Body: raw (JSON)
   - Content: `[{"session_duration": 130, "page_views": 6, "clicks": 9, "scroll_depth": 80, "time_on_site": 190}]`

**예제 파일**: `examples/postman_collection.json`

<br/>

### 6. HTTPie 사용
```bash
# CSV 파일 예측
http -f POST localhost:8000/predict file@test.csv

# JSON 예측
http POST localhost:8000/predict_batch session_duration:=130 page_views:=6 clicks:=9 scroll_depth:=80 time_on_site:=190
```

**예제 파일**: `examples/httpie_example.sh`

<br/>

### 7. 인라인 데이터로 빠른 테스트 (Docker 친화적)
```bash
# 테스트 파일 생성과 예측을 한 번에 실행
echo "session_duration,page_views,clicks,scroll_depth,time_on_site
130,6,9,80,190" > test.csv && curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@test.csv"
```

**예제 파일**: `examples/quick_test.sh`

<br/>

## API 문서

FastAPI 자동 생성 문서는 다음 URL에서 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

<br/>

## 예제

`examples/` 디렉토리는 API를 테스트하고 사용하는 다양한 방법들을 포함합니다:

### 예제 빠른 시작
```bash
# 예제 의존성 설치
pip install -r examples/requirements.txt

# Python 예제 실행
python examples/python_example.py

# 빠른 테스트 실행
./examples/quick_test.sh

# 웹 인터페이스 열기
open examples/web_example.html
```

### 사용 가능한 예제
- **Python**: 에러 처리가 포함된 완전한 스크립트 (`python_example.py`)
- **웹 인터페이스**: 인터랙티브 HTML 페이지 (`web_example.html`)
- **Postman**: 임포트할 수 있는 컬렉션 (`postman_collection.json`)
- **셸 스크립트**: 다양한 명령줄 예제
- **문서**: 자세한 사용법은 `examples/README-KR.md` 참조

### 예제 의존성
```bash
# Python 예제에 필수
pip install requests

# HTTPie 예제에 선택사항
pip install httpie
```

<br/>

## 컨테이너/이미지 정리

모든 Docker 컨테이너와 이미지를 정리하려면 아래 명령어를 사용하세요. (주의: 시스템의 모든 컨테이너/이미지가 삭제됩니다!)

```bash
# 모든 컨테이너 중지
docker ps -aq | xargs docker stop

# 모든 컨테이너 삭제
docker ps -aq | xargs docker rm

# 모든 이미지 삭제
docker images -aq | xargs docker rmi
```

> **주의:** 위 명령어는 시스템의 모든 컨테이너와 이미지를 삭제합니다. 꼭 필요한 경우에만 사용하세요.

