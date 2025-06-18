# MLOps Demo API 예제

이 디렉토리는 MLOps Demo API를 테스트하고 사용하기 위한 다양한 예제들을 포함합니다.

## 빠른 시작

1. **예제 의존성 설치**:
   ```bash
   pip install -r examples/requirements.txt
   ```

2. **API 서버 시작** (프로젝트 루트에서):
   ```bash
   python predict_api.py
   ```

3. **예제 실행**:
   ```bash
   # Python 예제
   python examples/python_example.py
   
   # 빠른 테스트
   ./examples/quick_test.sh
   
   # HTTPie 예제 (httpie 설치 필요)
   ./examples/httpie_example.sh
   ```

## 사용 가능한 예제

### 1. Python 예제 (`python_example.py`)
- 에러 처리가 포함된 완전한 Python 스크립트
- CSV와 JSON 엔드포인트 모두 테스트
- API 상태 확인 포함
- **사용법**: `python examples/python_example.py`

### 2. 웹 인터페이스 (`web_example.html`, `web_example.js`)
- API 테스트를 위한 인터랙티브 웹 인터페이스
- CSV 예측을 위한 파일 업로드
- 배치 예측을 위한 JSON 데이터 입력
- 실시간 결과 표시
- **사용법**: 웹 브라우저에서 `examples/web_example.html` 열기

### 3. Postman 컬렉션 (`postman_collection.json`)
- Postman에서 API 테스트를 위한 임포트 파일
- 모든 엔드포인트에 대한 사전 구성된 요청
- 바로 사용 가능한 테스트 데이터
- **사용법**: Postman 애플리케이션에 임포트

### 4. 셸 스크립트
- **`quick_test.sh`**: curl 명령어를 사용한 빠른 테스트
- **`httpie_example.sh`**: HTTPie 기반 테스트 (httpie 필요)

## 설치 요구사항

### 필수
- Python 3.8+
- requests 라이브러리: `pip install requests`

### 선택사항
- **HTTPie**: `pip install httpie` (httpie_example.sh용)
- **Postman**: [postman.com](https://www.postman.com/)에서 다운로드
- **웹 브라우저**: web_example.html용

## 테스트 데이터

모든 예제는 동일한 테스트 데이터 구조를 사용합니다:
```json
{
  "session_duration": 130,
  "page_views": 6,
  "clicks": 9,
  "scroll_depth": 80,
  "time_on_site": 190
}
```

## 문제 해결

1. **API가 실행되지 않음**: `python predict_api.py`로 시작
2. **포트 충돌**: 필요시 예제에서 포트 변경
3. **CORS 문제**: web_example.html을 로컬에서 사용
4. **파일을 찾을 수 없음**: 프로젝트 루트에서 실행 확인

## 예제 출력

성공적인 예측 응답:
```json
{
  "predictions": [1],
  "probabilities": [[0.0, 1.0]]
}
``` 