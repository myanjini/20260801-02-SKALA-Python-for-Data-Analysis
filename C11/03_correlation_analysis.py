import pandas as pd

df = pd.read_csv("visualization_sales.csv")
numeric_columns = [
    "quantity",
    "unit_price",
    "discount_rate",
    "ad_spend",
    "revenue",
    "cost",
    "profit",
    "satisfaction_score",
]

# 선형 관계를 측정합니다.
pearson = df[numeric_columns].corr(method="pearson")

# 순위 기반 단조 관계를 측정합니다.
spearman = df[numeric_columns].corr(method="spearman")

comparison = pd.DataFrame(
    {
        "pearson": pearson["revenue"],
        "spearman": spearman["revenue"],
    }
).sort_values("pearson", ascending=False)

print(comparison.round(3))
print("\n광고비와 매출의 피어슨 상관계수:", round(pearson.loc["ad_spend", "revenue"], 3))