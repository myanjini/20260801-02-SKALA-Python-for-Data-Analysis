import pandas as pd

sales = pd.DataFrame(
    {
        "region": ["서울", "서울", "부산", "부산"],
        "product_id": ["P01", "P02", "P01", "P03"],
        "amount": [100, 80, 120, 90],
    }
)

products = pd.DataFrame(
    {
        "product_id": ["P01", "P02", "P03"],
        "category": ["노트북", "모니터", "모니터"],
    }
)

# 판매 데이터의 여러 행이 하나의 상품 행과 결합되는 다대일 관계를 검증합니다.
merged = sales.merge(
    products,
    on="product_id",
    how="left",
    validate="many_to_one",
    indicator=True,
)

# 지역을 행, 상품군을 열로 배치하여 매출 합계를 계산합니다.
pivot = merged.pivot_table(
    index="region",
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="합계",
)

print("결합 상태")
print(merged["_merge"].value_counts())
print("\n피벗 결과")
print(pivot)