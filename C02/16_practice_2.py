"""컴프리헨션, Counter, defaultdict와 제너레이터를 종합 활용합니다."""

from collections import Counter, defaultdict


sales = [
    {"month": "2026-01", "region": "서울", "category": "도서", "amount": 1200},
    {"month": "2026-01", "region": "부산", "category": "식품", "amount": 800},
    {"month": "2026-01", "region": "서울", "category": "식품", "amount": 1800},
    {"month": "2026-02", "region": "대전", "category": "도서", "amount": 1500},
    {"month": "2026-02", "region": "서울", "category": "도서", "amount": 2200},
]


# 1,000 이상인 거래만 필터링합니다.
high_sales = [sale for sale in sales if sale["amount"] >= 1000]


# 고액 거래가 발생한 지역별 총매출을 계산합니다.
regions = {sale["region"] for sale in high_sales}

region_total = {
    region: sum(
        sale["amount"]
        for sale in high_sales
        if sale["region"] == region
    )
    for region in regions
}


# 전체 데이터의 지역별 거래 건수를 계산합니다.
region_count = Counter(sale["region"] for sale in sales)


# 카테고리별 금액을 그룹화합니다.
category_amounts = defaultdict(list)

for sale in sales:
    category_amounts[sale["category"]].append(sale["amount"])


def iter_large_sales(records, minimum_amount):
    """기준 금액을 초과하는 거래를 하나씩 생성합니다."""

    for record in records:
        if record["amount"] > minimum_amount:
            yield record


# 월과 카테고리를 복합 키로 사용하여 총매출을 집계합니다.
monthly_category_total = defaultdict(int)

for sale in sales:
    key = (sale["month"], sale["category"])
    monthly_category_total[key] += sale["amount"]


print("1,000 이상 거래:", high_sales)
print("지역별 총매출:", region_total)
print("지역별 거래 건수:", region_count)
print("카테고리별 금액:", dict(category_amounts))
print("1,000 초과 거래:", list(iter_large_sales(sales, 1000)))
print("월별 카테고리 매출:", dict(monthly_category_total))