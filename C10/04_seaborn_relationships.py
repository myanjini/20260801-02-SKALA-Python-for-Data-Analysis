import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/visualization_sales.csv")

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
correlation = df[numeric_columns].corr(numeric_only=True)

fig, axes = plt.subplots(1, 2, figsize=(16, 6), layout="constrained")

# 색상은 상품군, 점 크기는 수량을 표현합니다.
sns.scatterplot(
    data=df,
    x="ad_spend",
    y="revenue",
    hue="category",
    size="quantity",
    sizes=(30, 150),
    alpha=0.7,
    ax=axes[0],
)
axes[0].set_title("광고비와 매출의 관계")
axes[0].set_xlabel("광고비")
axes[0].set_ylabel("매출")

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="vlag",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    ax=axes[1],
)
axes[1].set_title("수치형 변수 상관계수")

plt.show()