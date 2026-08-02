import pandas as pd

df = pd.DataFrame(
    {
        "region": ["서울", "서울", "서울", "부산", "부산"],
        "category": ["노트북", "노트북", "모니터", "노트북", "모니터"],
        "customer_id": [1, 2, 1, 3, 4],
        "amount": [100, 150, 80, 120, 90],
    }
)

# 결과 열 이름=(집계 대상 열, 집계 함수) 형식의 named aggregation입니다.
summary = (
    df.groupby(["region", "category"], as_index=False)
    .agg(
        total_amount=("amount", "sum"),
        average_amount=("amount", "mean"),
        order_count=("amount", "size"),
        customer_count=("customer_id", "nunique"),
    )
    .sort_values("total_amount", ascending=False)
)

print(summary.to_string(index=False))