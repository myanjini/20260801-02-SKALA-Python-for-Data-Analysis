import numpy as np
import pandas as pd
from scipy import stats


def cohens_d_independent(group_a: np.ndarray, group_b: np.ndarray) -> float:
    """독립된 두 그룹의 표준화 평균 차이를 계산합니다."""
    n_a, n_b = len(group_a), len(group_b)
    pooled_variance = (
        ((n_a - 1) * group_a.var(ddof=1))
        + ((n_b - 1) * group_b.var(ddof=1))
    ) / (n_a + n_b - 2)
    return (group_a.mean() - group_b.mean()) / np.sqrt(pooled_variance)


df = pd.read_csv("visualization_sales.csv")
seoul = df.loc[df["region"] == "서울", "revenue"].dropna().to_numpy()
busan = df.loc[df["region"] == "부산", "revenue"].dropna().to_numpy()

# equal_var=False는 등분산을 가정하지 않는 Welch t-검정입니다.
test = stats.ttest_ind(seoul, busan, equal_var=False)
effect_size = cohens_d_independent(seoul, busan)
alpha = 0.05

print(f"서울 평균:{seoul.mean():,.0f}")
print(f"부산 평균:{busan.mean():,.0f}")
print(f"평균 차이:{seoul.mean() - busan.mean():,.0f}")
print(f"t 통계량:{test.statistic:.3f}")
print(f"p값:{test.pvalue:.4f}")
print(f"Cohen's d:{effect_size:.3f}")
print("판단:", "귀무가설 기각" if test.pvalue < alpha else "귀무가설 기각 못함")