"""로그를 이용하여 매출 집계 과정을 추적합니다."""

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s |%(message)s",
)

logger = logging.getLogger("sales")


def calculate_total(amounts: list[int | None]) -> int:
    """결측값을 제외한 매출 합계를 반환합니다."""

    logger.debug("입력 건수:%d", len(amounts))
    total = 0

    for index, amount in enumerate(amounts):
        if amount is None:
            logger.warning("%d번 데이터가 결측값이므로 제외합니다.", index)
            continue

        logger.debug("%d번 금액 처리:%d", index, amount)
        total += amount

    logger.info("매출 합계 계산 완료:%d", total)
    return total


result = calculate_total([1000, None, 2500])
print("결과:", result)