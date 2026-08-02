"""defaultdict와 Counter로 거래 데이터를 집계합니다."""

from collections import Counter, defaultdict


transactions = [
    {"region": "서울", "category": "도서", "amount": 15000},
    {"region": "부산", "category": "식품", "amount": 22000},
    {"region": "서울", "category": "식품", "amount": 18000},
    {"region": "서울", "category": "도서", "amount": 12000},
]

# 지역별 거래 건수를 계산합니다.
region_counts = Counter(
    transaction["region"]
    for transaction in transactions
)

# 카테고리별 거래 금액을 리스트로 그룹화합니다.
category_amounts = defaultdict(list)

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]
    category_amounts[category].append(amount)

print("지역별 거래 건수:", region_counts)
print("가장 많은 지역:", region_counts.most_common(1))
print("카테고리별 금액:", dict(category_amounts))