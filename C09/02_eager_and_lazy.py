import polars as pl

sales = pl.DataFrame(
    {
        "region": ["서울", "서울", "부산", "부산"],
        "amount": [100, 150, 120, 80],
    }
)

# Eager API는 각 메서드를 즉시 실행합니다.
eager_result = (
    sales
    .filter(pl.col("amount") >= 100)
    .group_by("region")
    .agg(pl.col("amount").sum().alias("total_amount"))
    .sort("region")
)

# lazy()는 기존 DataFrame을 LazyFrame으로 변환합니다.
lazy_query = (
    sales.lazy()
    .filter(pl.col("amount") >= 100)
    .group_by("region")
    .agg(pl.col("amount").sum().alias("total_amount"))
    .sort("region")
)

# collect()를 호출할 때 최적화된 계획을 실행합니다.
lazy_result = lazy_query.collect()

print(eager_result)
print("결과 일치:", eager_result.equals(lazy_result))