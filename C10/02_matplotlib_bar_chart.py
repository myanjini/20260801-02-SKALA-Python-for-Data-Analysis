import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/visualization_sales.csv")

region_sales = (
    df.groupby("region", observed=True)["revenue"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
bars = ax.bar(
    region_sales.index,
    region_sales.values,
    color="#4C78A8",
)

ax.set_title("지역별 총매출")
ax.set_xlabel("지역")
ax.set_ylabel("총매출")
ax.set_ylim(bottom=0)  # 막대 길이 비교를 위해 0 기준선을 유지합니다.
ax.grid(axis="y", alpha=0.2)

# 각 막대 위에 천 단위 구분 기호를 포함한 값을 표시합니다.
ax.bar_label(bars, labels=[f"{value:,.0f}" for value in region_sales.values], padding=3)

plt.show()