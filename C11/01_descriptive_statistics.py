import numpy as np
import pandas as pd

df = pd.read_csv("visualization_sales.csv", parse_dates=["order_date"])


def describe_numeric(series: pd.Series) -> pd.Series:
    """한 수치형 열의 핵심 기술통계를 계산합니다."""
    clean = series.dropna()
    q1 = clean.quantile(0.25)
    q3 = clean.quantile(0.75)

    return pd.Series(
        {
            "count": clean.size,
            "missing": series.isna().sum(),
            "mean": clean.mean(),
            "median": clean.median(),
            "std_sample": clean.std(ddof=1),  # 표본 표준편차입니다.
            "min": clean.min(),
            "q1": q1,
            "q3": q3,
            "max": clean.max(),
            "iqr": q3 - q1,
            "skewness": clean.skew(),
        }
    )


summary = pd.concat(
    {
        "revenue": describe_numeric(df["revenue"]),
        "profit": describe_numeric(df["profit"]),
    },
    axis=1,
).round(2)

print(summary)
print("\n매출 평균이 중앙값보다 큰가:", df["revenue"].mean() > df["revenue"].median())