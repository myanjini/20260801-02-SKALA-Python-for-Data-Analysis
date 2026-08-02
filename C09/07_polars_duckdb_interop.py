import duckdb
import polars as pl

raw = pl.DataFrame(
    {
        "region": ["서울", "서울", "부산", "부산"],
        "category": ["노트북", "모니터", "노트북", "모니터"],
        "amount": [100, None, 120, 80],
    }
)

# Polars에서 결측치 처리와 필터링을 수행합니다.
cleaned = (
    raw.lazy()
    .with_columns(pl.col("amount").fill_null(0))
    .filter(pl.col("amount") > 0)
    .collect()
)

# DuckDB는 현재 범위의 cleaned DataFrame을 직접 조회합니다.
sql = """
    SELECT
        region,
        SUM(amount) AS total_amount,
        COUNT(*) AS order_count
    FROM cleaned
    GROUP BY region
    ORDER BY total_amount DESC
"""

# pl()은 DuckDB 결과를 Polars DataFrame으로 반환합니다.
summary = duckdb.sql(sql).pl()
print(summary)