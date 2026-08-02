from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def load_data(path: Path) -> pd.DataFrame:
    """시각화용 CSV를 로딩하고 필수 열을 검증합니다."""
    df = pd.read_csv(path, parse_dates=["order_date"])
    required = {
        "month",
        "region",
        "category",
        "ad_spend",
        "revenue",
        "profit",
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"필수 열 누락:{sorted(missing)}")
    return df


def create_static_report(df: pd.DataFrame, output: Path) -> None:
    """4개 핵심 EDA 그래프를 하나의 PNG로 저장합니다."""
    monthly = df.groupby("month", as_index=False)["revenue"].sum()
    correlation = df[["ad_spend", "revenue", "cost", "profit"]].corr()

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10), layout="constrained")

    sns.lineplot(data=monthly, x="month", y="revenue", marker="o", ax=axes[0, 0])
    axes[0, 0].set_title("월별 총매출")
    axes[0, 0].tick_params(axis="x", rotation=45)

    sns.boxplot(data=df, x="category", y="revenue", hue="category", legend=False, ax=axes[0, 1])
    axes[0, 1].set_title("상품군별 매출 분포")

    sns.scatterplot(data=df, x="ad_spend", y="revenue", hue="category", alpha=0.7, ax=axes[1, 0])
    axes[1, 0].set_title("광고비와 매출")

    sns.heatmap(correlation, annot=True, fmt=".2f", cmap="vlag", center=0, ax=axes[1, 1])
    axes[1, 1].set_title("주요 변수 상관관계")

    fig.suptitle("2026년 판매 데이터 시각화 리포트", fontsize=16, fontweight="bold")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def create_interactive_report(df: pd.DataFrame, output: Path) -> None:
    """확대와 도구 설명이 가능한 산점도를 HTML로 저장합니다."""
    fig = px.scatter(
        df,
        x="ad_spend",
        y="revenue",
        color="category",
        size="quantity",
        hover_data=["order_id", "region", "channel", "profit"],
        title="광고비·매출 인터랙티브 분석",
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(output, include_plotlyjs="cdn")


def main() -> None:
    """정적·인터랙티브 시각화 리포트를 생성합니다."""
    df = load_data(Path("data/visualization_sales.csv"))
    print("행 수:", len(df))
    print("결측치:", df.isna().sum().sum())

    create_static_report(df, Path("output/visualization_report.png"))
    create_interactive_report(df, Path("output/visualization_report.html"))
    print("리포트 생성 완료")


if __name__ == "__main__":
    main()