import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

# 필요한 특성 컬럼 정의
FEATURE_COLUMNS = ['session_duration', 'page_views', 'clicks', 'scroll_depth', 'time_on_site']

def preprocess_data(input_file, output_dir):
    # 데이터 로드
    df = pd.read_csv(input_file)
    
    # 필요한 컬럼만 선택
    X = df[FEATURE_COLUMNS]
    y = df['target']
    
    # 결측치 처리
    X = X.fillna(X.mean())
    
    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 스케일링
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 전처리된 데이터 저장
    pd.DataFrame(X_train_scaled, columns=FEATURE_COLUMNS).to_csv(f'{output_dir}/X_train.csv', index=False)
    pd.DataFrame(X_test_scaled, columns=FEATURE_COLUMNS).to_csv(f'{output_dir}/X_test.csv', index=False)
    pd.DataFrame(y_train).to_csv(f'{output_dir}/y_train.csv', index=False)
    pd.DataFrame(y_test).to_csv(f'{output_dir}/y_test.csv', index=False)
    
    # 스케일러 저장
    joblib.dump(scaler, f'{output_dir}/scaler.pkl')
    
    print("전처리 완료:")
    print(f"- 학습 데이터: {len(X_train)} 샘플")
    print(f"- 테스트 데이터: {len(X_test)} 샘플")
    print(f"- 특성: {FEATURE_COLUMNS}")

if __name__ == '__main__':
    # 출력 디렉토리 생성
    os.makedirs('data', exist_ok=True)
    os.makedirs('model', exist_ok=True)
    
    # 데이터 전처리 실행
    preprocess_data('data/user_activity.csv', 'data') 