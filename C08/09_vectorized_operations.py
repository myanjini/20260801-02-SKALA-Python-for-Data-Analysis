import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "name": [" alice ", "Bob", " charlie"],
        "order_date": ["2026-07-01", "2026-07-15", "2026-08-01"],
        "amount": [80_000, 150_000, 320_000],
    }
)

# 문자열 접근자를 사용하여 공백 제거와 대문자 변환을 한 번에 수행합니다.
df["name_clean"] = df["name"].str.strip().str.upper()

# 날짜 자료형으로 변환한 후 월을 추출합니다.
df["order_date"] = pd.to_datetime(df["order_date"])
df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

# 여러 조건을 np.select에 전달하여 등급을 벡터화 방식으로 생성합니다.
conditions = [df["amount"] >= 300_000, df["amount"] >= 100_000]
choices = ["VIP", "우수"]
df["grade"] = np.select(conditions, choices, default="일반")

print(df[["name_clean", "order_month", "amount", "grade"]].to_string(index=False))