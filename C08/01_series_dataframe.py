import pandas as pd

# Series는 값과 인덱스로 구성된 1차원 자료구조입니다.
sales = pd.Series(
    [120_000, 180_000, 150_000],
    index=["서울", "부산", "대전"],
    name="매출",
)

# DataFrame은 열 이름을 키로 하는 여러 Series의 결합으로 볼 수 있습니다.
df = pd.DataFrame(
    {
        "region": ["서울", "부산", "대전"],
        "amount": [120_000, 180_000, 150_000],
        "orders": [12, 15, 10],
    }
)

# 한 열을 선택하면 Series를 반환합니다.
amount_series = df["amount"]

# 여러 열을 리스트로 선택하면 DataFrame을 반환합니다.
summary_df = df[["region", "amount"]]

print(sales)
print(type(amount_series).__name__)
print(type(summary_df).__name__)