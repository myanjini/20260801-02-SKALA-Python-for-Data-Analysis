import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("visualization_sales.csv")

# 두 범주형 변수의 관측 빈도표를 만듭니다.
observed = pd.crosstab(df["region"], df["category"])
test = stats.chi2_contingency(observed)

n = observed.to_numpy().sum()
min_dimension = min(observed.shape[0] - 1, observed.shape[1] - 1)
cramers_v = np.sqrt(test.statistic / (n * min_dimension))

print("관측 빈도")
print(observed)
print(f"\n카이제곱 통계량:{test.statistic:.3f}")
print(f"자유도:{test.dof}")
print(f"p값:{test.pvalue:.4f}")
print(f"최소 기대빈도:{test.expected_freq.min():.2f}")
print(f"Cramér's V:{cramers_v:.3f}")