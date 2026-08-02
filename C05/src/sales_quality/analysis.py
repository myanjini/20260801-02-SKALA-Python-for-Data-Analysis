"""테스트 가능한 매출 분석 함수를 제공합니다."""

from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class SalesRecord:
    """검증된 매출 레코드를 표현합니다."""

    region: str
    amount: float


def validate_record(record: SalesRecord) -> None:
    """매출 레코드가 업무 규칙을 만족하는지 확인합니다."""

    if not record.region.strip():
        raise ValueError("지역은 비어 있을 수 없습니다.")

    if record.amount <= 0:
        raise ValueError("금액은 0보다 커야 합니다.")


def filter_valid_records(
    records: Iterable[SalesRecord],
) -> tuple[list[SalesRecord], list[str]]:
    """정상 레코드와 오류 메시지를 분리하여 반환합니다."""

    valid_records: list[SalesRecord] = []
    errors: list[str] = []

    for index, record in enumerate(records, start=1):
        try:
            validate_record(record)
        except ValueError as error:
            errors.append(f"{index}번:{error}")
        else:
            valid_records.append(record)

    return valid_records, errors


def aggregate_by_region(records: Iterable[SalesRecord]) -> dict[str, float]:
    """지역별 매출 합계를 반환합니다."""

    totals: defaultdict[str, float] = defaultdict(float)

    for record in records:
        validate_record(record)
        totals[record.region.strip()] += record.amount

    return dict(totals)