"""매출 분석 함수의 정상·오류 경로를 검증합니다."""

import pytest

from sales_quality.analysis import (
    SalesRecord,
    aggregate_by_region,
    filter_valid_records,
    validate_record,
)


@pytest.fixture
def mixed_records() -> list[SalesRecord]:
    """정상과 오류 레코드가 섞인 목록을 반환합니다."""

    return [
        SalesRecord("서울", 1000),
        SalesRecord("부산", 2000),
        SalesRecord("서울", 3000),
        SalesRecord("", 500),
        SalesRecord("대전", -100),
    ]


def test_filter_valid_records(mixed_records: list[SalesRecord]) -> None:
    """정상 3건과 오류 2건으로 분리되는지 검증합니다."""

    valid_records, errors = filter_valid_records(mixed_records)

    assert len(valid_records) == 3
    assert len(errors) == 2


def test_aggregate_by_region() -> None:
    """지역별 매출 합계를 검증합니다."""

    records = [
        SalesRecord("서울", 1000),
        SalesRecord("부산", 2000),
        SalesRecord("서울", 3000),
    ]

    assert aggregate_by_region(records) == {
        "서울": 4000.0,
        "부산": 2000.0,
    }


@pytest.mark.parametrize(
    ("record", "message"),
    [
        (SalesRecord("", 1000), "지역은 비어"),
        (SalesRecord("서울", 0), "0보다 커야"),
        (SalesRecord("서울", -1), "0보다 커야"),
    ],
)
def test_validate_record_rejects_invalid_data(
    record: SalesRecord,
    message: str,
) -> None:
    """잘못된 레코드에서 ValueError가 발생하는지 검증합니다."""

    with pytest.raises(ValueError, match=message):
        validate_record(record)