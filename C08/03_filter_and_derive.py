import pandas as pd

df = pd.DataFrame(
    {
        "region": ["서울", "서울", "부산", "대전"],
        "category": ["노트북", "모니터", "노트북", "모니터"],
        "amount": [1_500_000, 400_000, 1_200_000, 350_000],
        "discount_rate": [0.10, 0.05, 0.08, 0.03],
    }
)

# 각 조건을 괄호로 감싸고 & 연산자로 결합합니다.
high_value = df.loc[
    (df["region"] == "서울") & (df["amount"] >= 500_000),
    ["region", "category", "amount", "discount_rate"],
].copy()

# 열 전체를 한 번에 계산하는 벡터화 연산입니다.
high_value["discount"] = high_value["amount"] * high_value["discount_rate"]
high_value["net_amount"] = high_value["amount"] - high_value["discount"]

print(high_value.to_string(index=False))