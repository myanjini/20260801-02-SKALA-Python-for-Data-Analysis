"""매출 계산 함수의 동작을 검증합니다."""

import pytest

from C05.src.sales import calculate_average


def test_calculate_average_returns_expected_value() -> None:
    """정상적인 금액 목록의 평균을 검증합니다."""

    result = calculate_average([1000.0, 2000.0, 3000.0])

    # approx()는 부동소수점의 작은 오차를 고려합니다.
    assert result == pytest.approx(2000.0)


def test_calculate_average_rejects_empty_list() -> None:
    """빈 목록에서 ValueError가 발생하는지 검증합니다."""

    with pytest.raises(ValueError, match="비어 있을 수 없습니다"):
        calculate_average([])


def test_calculate_average_rejects_negative_amount() -> None:
    """음수 금액에서 ValueError가 발생하는지 검증합니다."""

    with pytest.raises(ValueError, match="음수일 수 없습니다"):
        calculate_average([1000.0, -1.0])