import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 한글 폰트 설정
# plt.rcParams["font.family"] = "AppleGothic"  # macOS
plt.rcParams["font.family"] = "Malgun Gothic"  # Windows
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호 깨짐 방지

df = pd.read_csv("data/visualization_sales.csv")

# Seaborn의 공통 시각 스타일을 설정합니다.
sns.set_theme(style="whitegrid", context="notebook")

fig, axes = plt.subplots(1, 2, figsize=(14, 5), layout="constrained")

# 히스토그램과 밀도 곡선으로 전체 매출 분포를 확인합니다.
sns.histplot(
    data=df,
    x="revenue",
    bins=25,
    kde=True,
    color="#4C78A8",
    ax=axes[0],
)
axes[0].set_title("매출 분포")
axes[0].set_xlabel("매출")
axes[0].set_ylabel("빈도")

# 상품군별 중앙값·사분위수·이상치 후보를 비교합니다.
sns.boxplot(
    data=df,
    x="category",
    y="revenue",
    hue="category",
    legend=False,
    palette="Set2",
    ax=axes[1],
)
axes[1].set_title("상품군별 매출 분포")
axes[1].set_xlabel("상품군")
axes[1].set_ylabel("매출")

plt.show()
