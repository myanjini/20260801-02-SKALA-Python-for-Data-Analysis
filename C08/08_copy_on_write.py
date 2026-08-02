import pandas as pd

# Pandas 2.x에서 CoW 동작을 명시적으로 활성화합니다.
pd.options.mode.copy_on_write = True

df = pd.DataFrame(
    {
        "region": ["서울", "부산", "서울"],
        "amount": [100, 200, 150],
    }
)

# amount 칼럼을 float 타입으로 변경 후 연산
df["amount"] = df["amount"].astype(float)

# 원본을 수정하려면 행 조건과 대상 열을 하나의 loc 문장에 지정합니다.
df.loc[df["region"] == "서울", "amount"] *= 1.1

# 별도 분석 결과는 copy() 후 수정하여 의도를 명확히 합니다.
seoul = df.loc[df["region"] == "서울"].copy()
seoul = seoul.assign(amount_with_tax=seoul["amount"] * 1.1)

print("원본")
print(df)
print("\n서울 분석 결과")
print(seoul)