"""딕셔너리 데이터를 CSV 파일로 저장하고 읽습니다."""

import csv
from pathlib import Path


file_path = Path("sales.csv")
fieldnames = ["region", "category", "amount"]

sales = [
    {"region": "서울", "category": "도서", "amount": 150000},
    {"region": "부산", "category": "식품", "amount": 120000},
]

# newline=""는 CSV 처리 과정의 불필요한 빈 줄 생성을 방지합니다.
with file_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sales)


loaded_sales = []

with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # CSV에서 읽은 값은 문자열이므로 금액을 정수로 변환합니다.
        row["amount"] = int(row["amount"])
        loaded_sales.append(row)


print("읽은 데이터:", loaded_sales)
print("총매출:", sum(row["amount"] for row in loaded_sales))