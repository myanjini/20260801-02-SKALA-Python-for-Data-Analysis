import json
import platform
from pathlib import Path

import joblib
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ---------------------------------------------------------
# 1. 예제용 데이터 준비 및 모델 학습 (추가된 부분)
# ---------------------------------------------------------
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_state=42, random_state=42
)

# 모델 정의 및 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 예측 결과 및 임계값 예시
predictions = model.predict(X_test)
threshold = 100.0
# ---------------------------------------------------------

# 2. 모델 및 메타데이터 저장 경로 설정
model_dir = Path("output/model")
model_dir.mkdir(parents=True, exist_ok=True)

model_path = model_dir / "high_profit_pipeline.joblib"
metadata_path = model_dir / "metadata.json"

# 전처리와 분류기가 포함된 Pipeline(또는 모델) 전체를 저장합니다.
joblib.dump(model, model_path)

# 메타데이터 생성 및 저장
metadata = {
    "python_version": platform.python_version(),
    "scikit_learn_version": sklearn.__version__,
    "target": "high_profit",
    "profit_threshold": float(threshold),
    "feature_columns": list(X_test.columns),
}
metadata_path.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

# 3. 모델 로드 및 예측 결과 검증
loaded_model = joblib.load(model_path)
loaded_predictions = loaded_model.predict(X_test)

print("모델 파일:", model_path)
print("메타데이터 파일:", metadata_path)
print("예측 일치:", (predictions == loaded_predictions).all())