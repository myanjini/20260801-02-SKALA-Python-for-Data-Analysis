from pathlib import Path

import altair as alt
import pandas as pd

df = pd.read_csv("data/visualization_sales.csv")

# 범례에서 상품군을 선택하는 매개변수를 정의합니다.
category_selection = alt.selection_point(
    fields=["category"],
    bind="legend",
)

chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(
        x=alt.X("month:O", title="월", sort=None),
        y=alt.Y("sum(revenue):Q", title="총매출"),
        color=alt.Color("category:N", title="상품군"),
        opacity=alt.condition(category_selection, alt.value(1.0), alt.value(0.15)),
        tooltip=[
            alt.Tooltip("month:O", title="월"),
            alt.Tooltip("category:N", title="상품군"),
            alt.Tooltip("sum(revenue):Q", title="총매출", format=","),
        ],
    )
    .add_params(category_selection)
    .properties(
        width=760,
        height=400,
        title="상품군별 월별 매출",
    )
    .interactive()
)

output = Path("output/altair_monthly_sales.html")
output.parent.mkdir(exist_ok=True)
chart.save(output)
chart.show()