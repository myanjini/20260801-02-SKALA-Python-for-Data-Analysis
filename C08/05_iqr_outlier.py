import pandas as pd


def split_iqr_outliers(
    df: pd.DataFrame,
    column: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """IQR 기준의 정상 데이터와 이상치 후보를 분리합니다."""
    q1 = df[column].quantile(0.25)  # 제1사분위수를 계산합니다.
    q3 = df[column].quantile(0.75)  # 제3사분위수를 계산합니다.
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outlier_mask = ~df[column].between(lower, upper)
    normal = df.loc[~outlier_mask].copy()
    outliers = df.loc[outlier_mask].copy()

    print(f"허용 범위: {lower:.0f} ~{upper:.0f}")
    return normal, outliers


sales = pd.DataFrame(
    {"amount": [95, 100, 102, 105, 110, 115, 120, 1_000]}
)
normal, outliers = split_iqr_outliers(sales, "amount")

print("제거 전 행 수:", len(sales))
print("정상 행 수:", len(normal))
print("이상치 후보:", outliers["amount"].tolist())