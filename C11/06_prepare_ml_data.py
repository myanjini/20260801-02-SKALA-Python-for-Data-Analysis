import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("visualization_sales.csv")

# 타깃에 결측치가 있는 행은 학습에서 제외합니다.
model_df = df.dropna(subset=["profit"]).copy()

# 실습용 타깃은 이익이 중앙값 이상인지 나타냅니다.
# 실제 프로젝트에서는 업무 정의에 따라 고정된 기준을 사용해야 합니다.
profit_threshold = model_df["profit"].median()
model_df["high_profit"] = (model_df["profit"] >= profit_threshold).astype(int)

feature_columns = [
    "region",
    "category",
    "channel",
    "customer_segment",
    "quantity",
    "unit_price",
    "discount_rate",
    "ad_spend",
    "satisfaction_score",
]

# profit, revenue, cost는 타깃과 직접 연결되므로 피처에서 제외합니다.
X = model_df[feature_columns]
y = model_df["high_profit"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("이익 기준값:", profit_threshold)
print("학습 데이터:", X_train.shape)
print("테스트 데이터:", X_test.shape)
print("학습 타깃 비율:", y_train.value_counts(normalize=True).round(3).to_dict())
print("테스트 타깃 비율:", y_test.value_counts(normalize=True).round(3).to_dict())