from pathlib import Path

import duckdb
import polars as pl


def clean_sales(source: Path, destination: Path) -> None:
    """CSV를 지연 스캔하여 정제된 Parquet으로 저장합니다."""
    destination.parent.mkdir(parents=True, exist_ok=True)

    query = (
        pl.scan_csv(
            source,
            try_parse_dates=True,
        )
        # 실제 CSV에 존재하는 칼럼선택
        .select("order_date", "region", "amount", "memo")
        .filter(
            pl.col("order_date").is_not_null()
            & pl.col("amount").is_not_null()
            & (pl.col("amount") >= 0)
        )
        .with_columns(
            pl.col("region").fill_null("미상"),
            pl.col("memo").fill_null(""),
        )
        # order_id 대신 전체 칼럼(또는 주요 기준) 기준으로 중복 제거
        .unique(subset=["order_date", "region", "amount"], keep="last")
    )

    # collect 후 저장
    query.collect().write_parquet(destination)


def aggregate_sales(cleaned_path: Path, output_path: Path) -> pl.DataFrame:
    """정제 Parquet을 SQL로 집계하고 결과를 Polars로 반환합니다."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 실제 칼럼인 region 기준으로 집계 (category -> memo 또는 제거)
    sql = """
        SELECT
            region,
            SUM(amount) AS total_amount,
            ROUND(AVG(amount), 2) AS average_amount,
            COUNT(*) AS order_count
        FROM read_parquet(?)
        GROUP BY region
        ORDER BY total_amount DESC
    """

    with duckdb.connect() as connection:
        result = connection.execute(sql, [str(cleaned_path)]).pl()

    result.write_parquet(output_path)
    return result


def run_pipeline() -> pl.DataFrame:
    """정제와 집계 단계를 순서대로 실행합니다."""
    source = Path("data/sales.csv")
    cleaned = Path("data/sales_cleaned.parquet")
    summary = Path("output/sales_summary.parquet")

    clean_sales(source, cleaned)
    return aggregate_sales(cleaned, summary)


if __name__ == "__main__":
    print(run_pipeline())