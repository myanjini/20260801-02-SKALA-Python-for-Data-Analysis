"""콘솔과 파일에 로그를 기록하는 구조를 구성합니다."""

import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


def create_logger():
    """콘솔과 파일 핸들러가 연결된 로거를 반환합니다."""

    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    logger = logging.getLogger("sales_pipeline")
    logger.setLevel(logging.DEBUG)

    # 함수가 여러 번 호출되어도 핸들러를 중복 추가하지 않습니다.
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s |%(levelname)s |%(name)s |%(message)s"
    )

    # 콘솔에는 INFO 이상의 로그를 출력합니다.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 파일에는 DEBUG 이상의 로그를 저장하고 자정마다 파일을 교체합니다.
    file_handler = TimedRotatingFileHandler(
        filename=log_directory / "app.log",
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = create_logger()

logger.debug("상세 디버깅 정보를 기록합니다.")
logger.info("매출 파이프라인을 시작합니다.")

try:
    result = 10 / 0
except ZeroDivisionError:
    # exception()은 ERROR 로그와 호출 스택을 함께 기록합니다.
    logger.exception("매출 계산에 실패했습니다.")

logger.info("매출 파이프라인을 종료합니다.")