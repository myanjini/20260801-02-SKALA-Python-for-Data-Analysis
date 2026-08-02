"""테스트 대상 매출 계산 함수를 제공합니다."""


def calculate_average(amounts: list[float]) -> float:
    """금액 목록의 평균을 반환합니다."""

    if not amounts:
        raise ValueError("금액 목록은 비어 있을 수 없습니다.")

    if any(amount < 0 for amount in amounts):
        raise ValueError("금액은 음수일 수 없습니다.")

    return sum(amounts) / len(amounts)