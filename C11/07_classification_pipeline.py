import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("visualization_sales.csv").dropna(subset=["profit"]).copy()
threshold = df["profit"].median()
df["high_profit"] = (df["profit"] >= threshold).astype(int)

numeric_features = [
    "quantity",
    "unit_price",
    "discount_rate",
    "ad_spend",
    "satisfaction_score",
]
categorical_features = ["region", "category", "channel", "customer_segment"]

X = df[numeric_features + categorical_features]
y = df["high_profit"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 수치형 전처리는 결측치 대체 후 표준화를 수행합니다.
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

# 범주형 전처리는 결측치 대체 후 원-핫 인코딩을 수행합니다.
categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)

model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        (
            "classifier",
            LogisticRegression(max_iter=2_000, class_weight="balanced"),
        ),
    ]
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("혼동행렬")
print(confusion_matrix(y_test, predictions))
print("\n분류 보고서")
print(classification_report(y_test, predictions, digits=3))
print("ROC-AUC:", round(roc_auc_score(y_test, probabilities), 3))