"""Callable로 데이터 변환 함수의 타입을 정의합니다."""

from collections.abc import Callable


NumberTransform = Callable[[float], float]


def apply_transforms(
    value: float,
    transforms: list[NumberTransform],
) -> float:
    """입력값에 변환 함수를 순서대로 적용합니다."""

    result = value

    for transform in transforms:
        result = transform(result)

    return result


def add_tax(amount: float) -> float:
    """금액에 10%의 세금을 더합니다."""

    return amount * 1.1


def round_amount(amount: float) -> float:
    """금액을 가장 가까운 정수로 반올림합니다."""

    return round(amount)


pipeline: list[NumberTransform] = [add_tax, round_amount]
result: float = apply_transforms(12_345.0, pipeline)

print("변환 결과:", result)