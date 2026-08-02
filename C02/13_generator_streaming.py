"""제너레이터로 조건에 맞는 데이터를 하나씩 생성합니다."""

import sys


def filter_large_amounts(transactions, minimum_amount):
    """기준 금액 이상의 거래를 하나씩 생성합니다."""

    for transaction in transactions:
        if transaction["amount"] >= minimum_amount:
            # yield는 값을 반환한 후 함수 상태를 유지합니다.
            yield transaction


transactions = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 1500},
    {"id": 3, "amount": 2200},
    {"id": 4, "amount": 700},
]

# 리스트 컴프리헨션은 결과를 즉시 모두 생성합니다.
result_list = [
    transaction
    for transaction in transactions
    if transaction["amount"] >= 1000
]

# 제너레이터는 값을 요청할 때 생성합니다.
result_generator = filter_large_amounts(transactions, 1000)

print("리스트 객체 크기:", sys.getsizeof(result_list))
print("제너레이터 객체 크기:", sys.getsizeof(result_generator))

for transaction in result_generator:
    print("선택 거래:", transaction)