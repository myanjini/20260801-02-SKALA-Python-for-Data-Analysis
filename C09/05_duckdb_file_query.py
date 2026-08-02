from pathlib import Path

import duckdb
import polars as pl

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
parquet_path = data_dir / "sales.parquet"

pl.DataFrame(
    {
        "region": ["서울", "서울", "부산", "부산"],
        "amount": [100, 150, 120, 80],
    }
).write_parquet(parquet_path)

# 매개변수로 최소 매출을 전달하여 값과 SQL 문장을 분리합니다.
minimum_amount = 100
query = """
    SELECT
        region,
        SUM(amount) AS total_amount,
        ROUND(AVG(amount), 2) AS average_amount,
        COUNT(*) AS order_count
    FROM read_parquet(?)
    WHERE amount >= ?
    GROUP BY region
    ORDER BY total_amount DESC
"""

with duckdb.connect() as connection:
    result = connection.execute(
        query,
        [str(parquet_path), minimum_amount],
    ).fetchall()

print(result)