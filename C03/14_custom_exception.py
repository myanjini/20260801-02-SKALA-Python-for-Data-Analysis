"""사용자 정의 예외로 매출 데이터를 검증합니다."""


class DataValidationError(ValueError):
    """데이터가 업무 검증 규칙을 위반할 때 발생합니다."""


def validate_sales_record(record):
    """매출 레코드의 필수값과 금액을 검증합니다."""

    region = record.get("region", "").strip()
    amount = record.get("amount")

    if not region:
        raise DataValidationError("지역은 비어 있을 수 없습니다.")

    if not isinstance(amount, (int, float)):
        raise DataValidationError("금액은 숫자여야 합니다.")

    if amount <= 0:
        raise DataValidationError("금액은 0보다 커야 합니다.")

    return {
        "region": region,
        "amount": amount,
    }


records = [
    {"region": "서울", "amount": 1500},
    {"region": "", "amount": 800},
    {"region": "부산", "amount": -100},
]

valid_records = []
errors = []

for index, record in enumerate(records, start=1):
    try:
        valid_records.append(validate_sales_record(record))
    except DataValidationError as error:
        errors.append(f"{index}번 레코드:{error}")

print("정상 데이터:", valid_records)
print("오류:", errors)