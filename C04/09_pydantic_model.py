"""Pydantic v2로 매출 레코드를 검증하고 직렬화합니다."""

from datetime import date

from pydantic import BaseModel, Field, ValidationError


class SalesRecord(BaseModel):
    """검증된 매출 레코드를 표현합니다."""

    transaction_date: date
    region: str = Field(min_length=1, max_length=20)
    category: str = Field(min_length=1)
    amount: float = Field(gt=0)
    note: str | None = None


raw_record = {
    "transaction_date": "2026-08-01",
    "region": "서울",
    "category": "도서",
    "amount": "1500.5",
}

try:
    record = SalesRecord.model_validate(raw_record)
except ValidationError as error:
    print(error)
else:
    print("날짜 타입:", type(record.transaction_date).__name__)
    print("금액 타입:", type(record.amount).__name__)
    print("딕셔너리:", record.model_dump())
    print("JSON:", record.model_dump_json())