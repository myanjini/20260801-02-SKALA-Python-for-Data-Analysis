import polars as pl

sales = pl.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "region": ["서울", "서울", "부산", "부산"],
        "product_id": ["P01", "P02", "P01", "P03"],
        "amount": [100, 80, 120, 90],
    }
)

products = pl.DataFrame(
    {
        "product_id": ["P01", "P02", "P03"],
        "category": ["노트북", "모니터", "모니터"],
    }
)

# 여러 판매 행이 하나의 상품 행과 연결되는 다대일 조인입니다.
enriched = sales.join(
    products,
    on="product_id",
    how="left",
    validate="m:1",
)

summary = (
    enriched
    .group_by("region", "category")
    .agg(
        pl.col("amount").sum().alias("total_amount"),
        pl.col("amount").mean().alias("average_amount"),
        pl.col("order_id").n_unique().alias("order_count"),
    )
    .sort("total_amount", descending=True)
)

print(summary)