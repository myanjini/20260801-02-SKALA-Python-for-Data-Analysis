# 고급 자료구조 활용 실습
from collections import Counter, defaultdict, deque

# 1. deque를 활용한 양방향 큐 조작
queue = deque(["task1", "task2", "task3"])
queue.append("task4")        # 오른쪽 추가
queue.appendleft("priority") # 왼쪽 추가
print(f"큐 상태: {queue}")
queue.popleft()              # 맨 앞 작업 제거 O(1)

# 2. Counter를 이용한 범주 데이터 빈도 집계
categories = ["전자제품", "의류", "전자제품", "식품", "의류", "전자제품"]
category_counts = Counter(categories)
print(f"가장 많이 팔린 카테고리 상위 1개: {category_counts.most_common(1)}")

# 3. defaultdict를 활용한 그룹핑
sales_data = [("서울", 1000), ("부산", 2000), ("서울", 1500), ("인천", 800)]
grouped_sales = defaultdict(list)

for region, amount in sales_data:
    grouped_sales[region].append(amount)

print(f"지역별 매출 리스트: {dict(grouped_sales)}")