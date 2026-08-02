import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("visualization_sales.csv")
values = df["revenue"].dropna().to_numpy()

# t분포 기반 평균 신뢰구간을 계산합니다.
n = len(values)
sample_mean = values.mean()
standard_error = stats.sem(values)
t_interval = stats.t.interval(
    confidence=0.95,
    df=n - 1,
    loc=sample_mean,
    scale=standard_error,
)

# 분포 가정에 덜 의존하는 부트스트랩 구간을 계산합니다.
rng = np.random.default_rng(42)
bootstrap_means = np.array(
    [rng.choice(values, size=n, replace=True).mean() for _ in range(5_000)]
)
bootstrap_interval = np.quantile(bootstrap_means, [0.025, 0.975])

print(f"표본평균:{sample_mean:,.0f}")
print(f"t 95% 신뢰구간:{t_interval[0]:,.0f} ~{t_interval[1]:,.0f}")
print(
    "부트스트랩 95% 구간: "
    f"{bootstrap_interval[0]:,.0f} ~{bootstrap_interval[1]:,.0f}"
)