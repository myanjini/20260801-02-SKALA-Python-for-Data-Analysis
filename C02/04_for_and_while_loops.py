"""for와 while 반복문의 기본 사용법을 확인합니다."""


sales = [120000, 90000, 150000]
total_sales = 0

# enumerate()는 인덱스와 값을 함께 반환합니다.
for index, amount in enumerate(sales, start=1):
    print(f"{index}일차 매출:{amount}")
    total_sales += amount

print("총매출:", total_sales)


# while문에 사용할 카운터 변수입니다.
count = 3

while count > 0:
    print("남은 횟수:", count)

    # 조건을 False로 만들기 위해 값을 감소시킵니다.
    count -= 1

print("반복 종료")