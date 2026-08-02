"""CSV 매출 데이터를 검증하여 JSON으로 저장하는 종합 실습입니다."""

import csv
import json
import logging
import os
import time
from functools import wraps
from pathlib import Path


class DataValidationError(ValueError):
    """입력 데이터가 검증 규칙을 위반할 때 발생합니다."""


def timer(function):
    """함수의 실행 시간을 로그로 기록합니다."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return function(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            logging.info("%s 실행 시간:%.6f초", function.__name__, elapsed)

    return wrapper


def validate_row(row, line_number):
    """CSV 행을 검증하고 타입이 변환된 딕셔너리를 반환합니다."""

    region = row.get("region", "").strip()

    if not region:
        raise DataValidationError(f"{line_number}행: 지역 누락")

    try:
        amount = int(row.get("amount", ""))
    except ValueError as error:
        raise DataValidationError(
            f"{line_number}행: 금액 형식 오류"
        ) from error

    if amount <= 0:
        raise DataValidationError(f"{line_number}행: 금액은 0보다 커야 함")

    return {
        "region": region,
        "category": row.get("category", "미분류").strip() or "미분류",
        "amount": amount,
    }


def read_valid_rows(file_path):
    """CSV에서 정상 행을 하나씩 생성합니다."""

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"region", "category", "amount"}
        actual_columns = set(reader.fieldnames or [])

        if not required_columns.issubset(actual_columns):
            missing = required_columns - actual_columns
            raise DataValidationError(f"필수 열 누락:{sorted(missing)}")

        for line_number, row in enumerate(reader, start=2):
            try:
                yield validate_row(row, line_number)
            except DataValidationError as error:
                logging.warning("데이터 제외:%s", error)


@timer
def run_pipeline(input_path, output_path):
    """입력 CSV를 검증하고 정상 데이터를 JSON으로 저장합니다."""

    valid_rows = list(read_valid_rows(input_path))

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(valid_rows, file, ensure_ascii=False, indent=2)

    logging.info("정상 데이터%d건 저장", len(valid_rows))

    return valid_rows


def main():
    """환경변수에서 경로를 읽고 파이프라인을 실행합니다."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s |%(levelname)s |%(message)s",
    )

    input_path = Path(os.getenv("INPUT_CSV", "sales.csv"))
    output_path = Path(os.getenv("OUTPUT_JSON", "output/valid_sales.json"))

    try:
        records = run_pipeline(input_path, output_path)
    except FileNotFoundError:
        logging.error("입력 파일이 없습니다:%s", input_path)
    except DataValidationError as error:
        logging.error("파일 구조 오류:%s", error)
    except OSError:
        logging.exception("파일 처리 중 운영체제 오류 발생")
    else:
        print("저장 건수:", len(records))
        print("출력 파일:", output_path)


if __name__ == "__main__":
    main()