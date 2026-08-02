"""간단한 데이터 탐색 과정을 확인하는 예제입니다."""


# 분석할 일별 매출 데이터입니다.
daily_sales = [120000, 150000, 98000, 175000, 143000]

# len()은 데이터의 개수를 반환합니다.
sales_count = len(daily_sales)

# sum()은 리스트에 저장된 숫자의 합계를 반환합니다.
total_sales = sum(daily_sales)

# 평균 매출을 계산합니다.
average_sales = total_sales / sales_count

# min()과 max()는 각각 최솟값과 최댓값을 반환합니다.
minimum_sales = min(daily_sales)
maximum_sales = max(daily_sales)

print("데이터 개수:", sales_count)
print("총매출:", total_sales)
print("평균 매출:", average_sales)
print("최소 매출:", minimum_sales)
print("최대 매출:", maximum_sales)

# 리스트 컴프리헨션으로 평균 이상의 매출만 추출합니다.
high_sales = [
    sales
    for sales in daily_sales
    if sales >= average_sales
]

print("평균 이상 매출:", high_sales)