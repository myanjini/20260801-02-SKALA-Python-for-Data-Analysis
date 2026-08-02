"""중단점에서 반복문의 변수 상태를 확인합니다."""


def calculate_positive_total(amounts: list[int]) -> int:
    """양수인 금액만 더하여 반환합니다."""

    total = 0

    for index, amount in enumerate(amounts):
        # 디버깅할 때 아래 주석을 해제합니다.
        # breakpoint()

        if amount <= 0:
            continue

        total += amount
        print(f"{index}번 처리 후 합계:{total}")

    return total


result = calculate_positive_total([1000, -200, 3000])
print("최종 합계:", result)
