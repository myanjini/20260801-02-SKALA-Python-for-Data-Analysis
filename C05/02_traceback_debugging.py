"""중첩된 함수 호출에서 발생한 오류를 기록합니다."""

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s |%(message)s",
)

logger = logging.getLogger("average")


def divide(total: float, count: int) -> float:
    """합계를 개수로 나누어 반환합니다."""

    return total / count


def calculate_average(values: list[float]) -> float:
    """숫자 목록의 평균을 계산합니다."""

    return divide(sum(values), len(values))


def create_report(values: list[float]) -> str:
    """평균값을 보고서 문자열로 반환합니다."""

    average = calculate_average(values)
    return f"평균:{average:.1f}"


try:
    print(create_report([]))
except ZeroDivisionError:
    # 현재 예외 메시지와 호출 스택을 함께 기록합니다.
    logger.exception("빈 데이터의 평균을 계산할 수 없습니다.")