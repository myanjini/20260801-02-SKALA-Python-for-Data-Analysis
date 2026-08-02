from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/visualization_sales.csv")
monthly = df.groupby("month", as_index=False)["revenue"].sum()
regional = (
    df.groupby("region", as_index=False, observed=True)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 10), layout="constrained")

sns.histplot(data=df, x="revenue", bins=25, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("매출 분포")

sns.boxplot(data=df, x="category", y="profit", hue="category", legend=False, ax=axes[0, 1])
axes[0, 1].set_title("상품군별 이익 분포")

sns.lineplot(data=monthly, x="month", y="revenue", marker="o", ax=axes[1, 0])
axes[1, 0].set_title("월별 총매출")
axes[1, 0].tick_params(axis="x", rotation=45)

sns.barplot(data=regional, x="region", y="revenue", hue="region", legend=False, ax=axes[1, 1])
axes[1, 1].set_title("지역별 총매출")

fig.suptitle("2026년 판매 데이터 EDA", fontsize=16, fontweight="bold")

output = Path("output/sales_eda_dashboard.png")
output.parent.mkdir(exist_ok=True)
fig.savefig(output, dpi=180, bbox_inches="tight")
plt.show()