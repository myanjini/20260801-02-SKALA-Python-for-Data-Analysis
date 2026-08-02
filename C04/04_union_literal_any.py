"""Union, Literal과 Any의 사용 방법을 비교합니다."""

from typing import Any, Literal


SortDirection = Literal["asc", "desc"]


def normalize_id(value: str | int) -> str:
    """문자열 또는 정수 ID를 표준 문자열로 변환합니다."""

    return str(value).strip().upper()


def sort_scores(
    scores: list[int],
    direction: SortDirection = "desc",
) -> list[int]:
    """허용된 방향에 따라 점수를 정렬합니다."""

    return sorted(scores, reverse=direction == "desc")


def normalize_external_value(value: Any) -> str:
    """타입 정보가 없는 외부 값을 문자열로 변환합니다."""

    if value is None:
        return ""

    return str(value).strip()


print("문자열 ID:", normalize_id(" user-01 "))
print("정수 ID:", normalize_id(1001))
print("내림차순:", sort_scores([80, 95, 70]))
print("외부 값:", normalize_external_value(3.14))