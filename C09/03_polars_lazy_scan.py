from pathlib import Path

import polars as pl

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
csv_path = data_dir / "sales.csv"

# 실습용 입력 파일을 생성합니다.
pl.DataFrame(
    {
        "order_date": ["2026-07-01", "2026-07-02", "2026-08-01", "2026-08-02"],
        "region": ["서울", "부산", "서울", "부산"],
        "amount": [100, 80, 150, 120],
        "memo": ["A", "B", "C", "D"],
    }
).write_csv(csv_path)

# scan_csv는 파일을 즉시 모두 읽지 않고 LazyFrame을 반환합니다.
query = (
    pl.scan_csv(csv_path, try_parse_dates=True)
    # memo 열은 선택하지 않으므로 읽기 단계에서 제외될 수 있습니다.
    .select("order_date", "region", "amount")
    # 필터 조건은 스캔 단계로 내려갈 수 있습니다.
    .filter(pl.col("amount") >= 100)
    .with_columns(
        pl.col("order_date").dt.strftime("%Y-%m").alias("month")
    )
    .group_by("month", "region")
    .agg(pl.col("amount").sum().alias("total_amount"))
    .sort("month", "region")
)

print("최적화된 실행 계획")
print(query.explain(optimized=True))

result = query.collect()
print("\n집계 결과")
print(result)