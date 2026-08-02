import polars as pl

sales = pl.DataFrame(
    {
        "region": ["서울", "서울", "부산", "대전"],
        "category": ["노트북", "모니터", "노트북", "모니터"],
        "amount": [1_500_000, 400_000, 1_200_000, 350_000],
        "discount_rate": [0.10, 0.05, 0.08, 0.03],
    }
)

result = (
    sales
    # 서울이면서 매출이 500,000 이상인 행을 선택합니다.
    .filter(
        (pl.col("region") == "서울")
        & (pl.col("amount") >= 500_000)
    )
    # 여러 파생 열을 표현식으로 생성합니다.
    .with_columns(
        (pl.col("amount") * pl.col("discount_rate")).alias("discount"),
        pl.when(pl.col("amount") >= 1_000_000)
        .then(pl.lit("고액"))
        .otherwise(pl.lit("일반"))
        .alias("sales_grade"),
    )
    .with_columns(
        (pl.col("amount") - pl.col("discount")).alias("net_amount")
    )
    .select("region", "category", "amount", "discount", "net_amount", "sales_grade")
)

print(result)