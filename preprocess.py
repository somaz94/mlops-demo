import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_file, output_dir):
    # 데이터 로드
    df = pd.read_csv(input_file)
    
    # 예시 전처리 (실제 데이터에 맞게 수정 필요)
    # 결측치 처리
    df = df.fillna(df.mean())
    
    # 특성과 타겟 분리
    X = df.drop('target', axis=1)  # 'target' 컬럼을 타겟으로 가정
    y = df['target']
    
    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 스케일링
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 전처리된 데이터 저장
    pd.DataFrame(X_train_scaled).to_csv(f'{output_dir}/X_train.csv', index=False)
    pd.DataFrame(X_test_scaled).to_csv(f'{output_dir}/X_test.csv', index=False)
    pd.DataFrame(y_train).to_csv(f'{output_dir}/y_train.csv', index=False)
    pd.DataFrame(y_test).to_csv(f'{output_dir}/y_test.csv', index=False)
    
    # 스케일러 저장
    import joblib
    joblib.dump(scaler, f'{output_dir}/scaler.pkl')

if __name__ == '__main__':
    preprocess_data('data/user_activity.csv', 'data') 