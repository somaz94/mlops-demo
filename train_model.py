import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(data_dir, model_dir):
    # 데이터 로드
    X_train = pd.read_csv(f'{data_dir}/X_train.csv')
    y_train = pd.read_csv(f'{data_dir}/y_train.csv')
    X_test = pd.read_csv(f'{data_dir}/X_test.csv')
    y_test = pd.read_csv(f'{data_dir}/y_test.csv')
    
    # 모델 학습
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    
    # 모델 평가
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy:.4f}')
    print('\nClassification Report:')
    print(classification_report(y_test, y_pred))
    
    # 모델 저장
    joblib.dump(model, f'{model_dir}/model.pkl')
    print(f'Model saved to {model_dir}/model.pkl')

if __name__ == '__main__':
    train_model('data', 'model') 