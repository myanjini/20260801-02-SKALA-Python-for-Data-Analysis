"""매개변수화로 여러 점수 경계를 검증합니다."""

import pytest


def determine_grade(score: int) -> str:
    """점수에 따른 등급을 반환합니다."""

    if not 0 <= score <= 100:
        raise ValueError("점수 범위 오류")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "D"


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (0, "D"),
    ],
)
def test_determine_grade(score: int, expected: str) -> None:
    """각 점수의 기대 등급을 검증합니다."""

    assert determine_grade(score) == expected


@pytest.mark.parametrize("invalid_score", [-1, 101])
def test_determine_grade_rejects_invalid_score(invalid_score: int) -> None:
    """허용 범위 밖의 점수를 거부하는지 검증합니다."""

    with pytest.raises(ValueError, match="범위 오류"):
        determine_grade(invalid_score)