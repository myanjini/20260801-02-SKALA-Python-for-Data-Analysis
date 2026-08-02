"""dataclass와 TypedDict로 매출 데이터의 구조를 정의합니다."""

from dataclasses import dataclass, field
from typing import TypedDict


class RawSalesRecord(TypedDict):
    """입력 딕셔너리의 키와 값 타입을 정의합니다."""

    month: str
    region: str
    amount: int


@dataclass
class SalesSummary:
    """지역별 매출 집계 결과를 표현합니다."""

    region: str
    total_amount: int = 0

    # default_factory는 인스턴스별 독립 리스트를 생성합니다.
    source_months: list[str] = field(default_factory=list)

    def add(self, month, amount):
        """월과 매출 금액을 집계 결과에 추가합니다."""

        self.total_amount += amount
        self.source_months.append(month)


raw_record: RawSalesRecord = {
    "month": "2026-01",
    "region": "서울",
    "amount": 150000,
}

summary = SalesSummary(region=raw_record["region"])
summary.add(raw_record["month"], raw_record["amount"])

print(summary)
print("총매출:", summary.total_amount)