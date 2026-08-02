from pathlib import Path

import pandas as pd


REQUIRED_SALES_COLUMNS = {
    "order_id",
    "order_date",
    "region",
    "product_id",
    "amount",
}


def validate_columns(df: pd.DataFrame, required: set[str]) -> None:
    """필수 열이 없으면 분석을 중단합니다."""
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"필수 열 누락:{sorted(missing)}")


def remove_iqr_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """IQR 범위 안의 행만 독립된 DataFrame으로 반환합니다."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    return df.loc[df[column].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)].copy()


def run_pipeline(sales_path: Path, products_path: Path) -> pd.DataFrame:
    """판매 데이터를 정제·결합·집계합니다."""
    sales = pd.read_csv(sales_path, parse_dates=["order_date"])
    products = pd.read_csv(products_path, dtype={"product_id": "string"})
    validate_columns(sales, REQUIRED_SALES_COLUMNS)

    # 필수 식별값의 결측 행과 주문 중복을 제거합니다.
    cleaned = (
        sales.dropna(subset=["order_id", "order_date", "product_id", "amount"])
        .drop_duplicates(subset=["order_id"], keep="last")
        .copy()
    )
    cleaned["region"] = cleaned["region"].fillna("미상")
    cleaned = remove_iqr_outliers(cleaned, "amount")

    # 상품 마스터는 product_id당 한 행이어야 합니다.
    enriched = cleaned.merge(
        products[["product_id", "category"]],
        on="product_id",
        how="left",
        validate="many_to_one",
    )
    enriched["category"] = enriched["category"].fillna("미분류")

    summary = (
        enriched.groupby(["region", "category"], as_index=False)
        .agg(
            total_amount=("amount", "sum"),
            average_amount=("amount", "mean"),
            order_count=("order_id", "nunique"),
        )
        .sort_values("total_amount", ascending=False)
    )
    return summary


if __name__ == "__main__":
    result = run_pipeline(Path("data/pandas_practice_sales.csv"), Path("data/pandas_practice_products.csv"))
    output_path = Path("output/sales_summary.parquet")
    output_path.parent.mkdir(exist_ok=True)
    result.to_parquet(output_path, index=False)
    print(result.to_string(index=False))