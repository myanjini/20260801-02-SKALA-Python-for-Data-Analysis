"""Ruff 린팅 실습을 위한 코드입니다."""

import os  # 사용하지 않는 import이므로 F401 검사 대상입니다.


def calculate_total(amounts: list[int]) -> int:
    """금액 목록의 합계를 반환합니다."""

    unused_value = 10  # 사용하지 않는 지역 변수의 검사 대상이 될 수 있습니다.
    return sum(amounts)


print(calculate_total([1000, 2000]))