"""CSV 파일을 읽어 Pydantic으로 검증하고 정상 데이터를 저장합니다."""

import csv
import json
import logging
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError, field_validator


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s |%(message)s",
)

logger = logging.getLogger("validation_pipeline")


class SalesRecord(BaseModel):
    """검증된 월별 지역 매출 레코드를 표현합니다."""

    month: str = Field(min_length=1)
    region: str = Field(min_length=1)
    category: str = Field(min_length=1)
    amount: float = Field(gt=0)

    @field_validator("month", "region", "category")
    @classmethod
    def strip_required_text(cls, value: str) -> str:
        """필수 문자열의 공백을 제거하고 빈 값을 차단합니다."""

        clean_value = value.strip()

        if not clean_value:
            raise ValueError("필수 문자열은 비어 있을 수 없습니다.")

        return clean_value


def safe_load_csv(file_path: Path) -> list[dict[str, str]] | None:
    """CSV 파일을 안전하게 읽고 실패하면 None을 반환합니다."""

    try:
        with file_path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except FileNotFoundError:
        logger.error("파일을 찾을 수 없습니다:%s", file_path)
        return None

    except (OSError, UnicodeError, csv.Error):
        logger.exception("CSV 파일을 읽지 못했습니다:%s", file_path)
        return None

    else:
        logger.info("CSV 파일%d행을 읽었습니다.", len(rows))
        return rows

    finally:
        logger.debug("CSV 읽기 작업 종료:%s", file_path)


def validate_rows(
    rows: list[dict[str, str]],
) -> tuple[list[SalesRecord], list[dict[str, object]]]:
    """CSV 행을 검증하여 정상 모델과 오류 정보를 반환합니다."""

    valid_records: list[SalesRecord] = []
    errors: list[dict[str, object]] = []

    for row_number, row in enumerate(rows, start=2):
        try:
            record = SalesRecord.model_validate(row)
        except ValidationError as error:
            errors.append(
                {
                    "row_number": row_number,
                    "errors": error.errors(),
                }
            )
            logger.warning("%d행 검증 실패", row_number)
        else:
            valid_records.append(record)

    return valid_records, errors


def save_valid_records(
    records: list[SalesRecord],
    output_path: Path,
) -> None:
    """정상 모델을 JSON 파일로 저장합니다."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    serializable_records = [
        record.model_dump(mode="json")
        for record in records
    ]

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(serializable_records, file, ensure_ascii=False, indent=2)


def reload_records(output_path: Path) -> list[dict[str, object]]:
    """저장된 JSON 파일을 다시 읽어 반환합니다."""

    with output_path.open("r", encoding="utf-8") as file:
        loaded: list[dict[str, object]] = json.load(file)

    return loaded


def main() -> None:
    """검증 파이프라인의 전체 실행 흐름을 관리합니다."""

    input_path = Path("sales.csv")
    output_path = Path("output/valid_sales.json")

    rows = safe_load_csv(input_path)

    if rows is None:
        return

    valid_records, errors = validate_rows(rows)
    save_valid_records(valid_records, output_path)
    reloaded_records = reload_records(output_path)

    print("정상 데이터:", len(valid_records))
    print("오류 데이터:", len(errors))
    print("재로딩 데이터:", len(reloaded_records))

    # 예상 결과를 자동으로 검증합니다.
    assert len(valid_records) == len(reloaded_records)


if __name__ == "__main__":
    main()