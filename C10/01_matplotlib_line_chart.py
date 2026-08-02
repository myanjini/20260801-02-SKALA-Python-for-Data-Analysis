from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/visualization_sales.csv", parse_dates=["order_date"])

# 월별 합계를 먼저 계산하여 시각화 입력을 명확하게 만듭니다.
monthly = (
    df.groupby("month", as_index=False, observed=True)
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
    )
)

fig, ax = plt.subplots(figsize=(11, 5), layout="constrained")

# Axes에 매출과 이익 선을 각각 작성합니다.
ax.plot(monthly["month"], monthly["revenue"], marker="o", label="매출")
ax.plot(monthly["month"], monthly["profit"], marker="s", label="이익")

ax.set_title("2026년 월별 매출과 이익")
ax.set_xlabel("월")
ax.set_ylabel("금액")
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.25)
ax.legend()

# 화면 표시와 별도로 재사용 가능한 이미지 파일을 저장합니다.
output = Path("output/monthly_revenue_profit.png")
output.parent.mkdir(exist_ok=True)
fig.savefig(output, dpi=150, bbox_inches="tight")
plt.show()