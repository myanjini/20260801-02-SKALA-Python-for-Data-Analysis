"""mypy가 탐지할 수 있는 타입 오류 예제입니다."""


def compute_average(values: list[float]) -> float:
    """실수 목록의 평균을 반환합니다."""

    return sum(values) / len(values)


valid_values: list[float] = [10.0, 20.0, 30.0]
print(compute_average(valid_values))

# 아래 코드는 정수 대신 문자열을 포함하므로 mypy 오류가 발생합니다.
invalid_values: list[float] = [10.0, "20", 30.0]  # type: ignore[list-item]

# 타입 검사를 학습하기 위한 코드이며 실제 호출은 수행하지 않습니다.