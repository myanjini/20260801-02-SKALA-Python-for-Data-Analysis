import duckdb
import polars as pl

sales = pl.DataFrame(
    {
        "region": ["서울", "서울", "부산", "부산"],
        "order_id": [101, 102, 103, 104],
        "amount": [100, 150, 120, 80],
    }
)

query = """
    SELECT
        region,
        order_id,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY region
            ORDER BY amount DESC, order_id
        ) AS sales_rank,
        SUM(amount) OVER (
            PARTITION BY region
            ORDER BY amount DESC, order_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cumulative_amount
    FROM sales
    ORDER BY region, sales_rank
"""

# DuckDB Python 클라이언트는 현재 범위의 DataFrame을 이름으로 조회할 수 있습니다.
result = duckdb.sql(query).pl()
print(result)