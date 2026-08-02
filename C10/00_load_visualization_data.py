from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/visualization_sales.csv")

# 날짜 열은 로딩 시 datetime64 자료형으로 변환합니다.
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

# 반복되는 문자열 열은 category 자료형으로 변환할 수 있습니다.
category_columns = [
    "region",
    "category",
    "channel",
    "customer_segment",
]
df[category_columns] = df[category_columns].astype("category")

print("데이터 크기:", df.shape)
print("기간:", df["order_date"].min(), "~", df["order_date"].max())
print("\n결측치 수")
print(df.isna().sum()[df.isna().sum() > 0])
print("\n수치형 기술통계")
print(df[["revenue", "profit", "ad_spend"]].describe().round(1))