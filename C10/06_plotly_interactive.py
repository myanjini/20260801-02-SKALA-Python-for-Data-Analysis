from pathlib import Path

import pandas as pd
import plotly.express as px

df = pd.read_csv("data/visualization_sales.csv")

fig = px.scatter(
    df,
    x="ad_spend",
    y="revenue",
    color="category",
    size="quantity",
    hover_name="order_id",
    hover_data={
        "region": True,
        "channel": True,
        "profit": ":,.0f",
        "ad_spend": ":,.0f",
        "revenue": ":,.0f",
    },
    facet_col="channel",
    title="채널별 광고비와 매출의 관계",
    labels={
        "ad_spend": "광고비",
        "revenue": "매출",
        "category": "상품군",
        "quantity": "수량",
        "channel": "채널",
    },
)

fig.update_traces(marker={"opacity": 0.7})
fig.update_layout(legend_title_text="상품군")

output = Path("output/interactive_ad_revenue.html")
output.parent.mkdir(exist_ok=True)
fig.write_html(output, include_plotlyjs="cdn")
fig.show()