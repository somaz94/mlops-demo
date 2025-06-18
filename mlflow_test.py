import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 데이터 준비
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MLflow 자동 로깅 활성화
mlflow.sklearn.autolog()

# 실험 추적 시작
with mlflow.start_run(run_name="rf_iris_demo"):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print("Test Accuracy:", acc)
    mlflow.log_metric("test_accuracy", acc) 