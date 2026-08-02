from pathlib import Path

import pandas as pd


def inspect_dataframe(df: pd.DataFrame) -> None:
    """DataFrame의 구조와 품질을 빠르게 확인합니다."""
    print("크기:", df.shape)  # (행 수, 열 수)를 출력합니다.
    print("열:", df.columns.tolist())  # 열 이름을 리스트로 확인합니다.
    print("\n자료형:")
    print(df.dtypes)  # 열별 자료형을 확인합니다.
    print("\n결측치 수:")
    print(df.isna().sum())  # 열별 결측치 개수를 계산합니다.
    print("\n수치형 기술통계:")
    print(df.describe().round(2))


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
csv_path = data_dir / "sales.csv"

source = pd.DataFrame(
    {
        "date": ["2026-07-01", "2026-07-02", "2026-07-03", "2026-07-04"],
        "region": ["서울", "부산", "서울", "대전"],
        "amount": [120_000, 180_000, None, 150_000],
        "orders": [12, 15, 11, 10],
    }
)
source.to_csv(csv_path, index=False, encoding="utf-8-sig")

# 날짜 열을 로딩 단계에서 datetime64 자료형으로 변환합니다.
df = pd.read_csv(csv_path, parse_dates=["date"])
inspect_dataframe(df)