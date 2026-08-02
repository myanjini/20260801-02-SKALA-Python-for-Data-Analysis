import pandas as pd

df = pd.DataFrame(
    {
        "order_id": [101, 102, 102, 103, None],
        "region": ["서울", "부산", "부산", None, "대전"],
        "amount": [100_000, 200_000, 200_000, None, 150_000],
    }
)

print("처리 전 결측치")
print(df.isna().sum())

# 주문 번호가 없는 행은 식별할 수 없으므로 제거합니다.
cleaned = df.dropna(subset=["order_id"]).copy()

# amount의 중앙값을 계산하여 결측값을 대체합니다.
amount_median = cleaned["amount"].median()
cleaned["amount"] = cleaned["amount"].fillna(amount_median)

# 지역 결측값은 별도 범주로 보존합니다.
cleaned["region"] = cleaned["region"].fillna("미상")

# 업무 키인 order_id가 같은 중복 행은 첫 번째 행만 유지합니다.
cleaned = cleaned.drop_duplicates(subset=["order_id"], keep="first")

print("\n처리 후")
print(cleaned.to_string(index=False))