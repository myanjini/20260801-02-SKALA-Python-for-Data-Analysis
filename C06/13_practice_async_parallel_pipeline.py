"""비동기 수집과 프로세스 기반 계산을 연결합니다."""

import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s |%(message)s",
)

logger = logging.getLogger("pipeline")


@dataclass(frozen=True)
class SourceConfig:
    """수집할 데이터 소스의 설정을 표현합니다."""

    name: str
    delay: float
    values: list[int]
    should_fail: bool = False


async def collect_source(config: SourceConfig) -> dict[str, object]:
    """외부 데이터 수집을 비동기 대기로 모의합니다."""

    try:
        await asyncio.sleep(config.delay)

        if config.should_fail:
            raise ConnectionError("수집 연결 실패")

        logger.info("%s 수집 완료", config.name)

        return {
            "name": config.name,
            "status": "success",
            "values": config.values,
        }
    except ConnectionError as error:
        logger.error("%s 수집 실패:%s", config.name, error)

        return {
            "name": config.name,
            "status": "error",
            "error": str(error),
        }


def calculate_statistics(values: list[int]) -> dict[str, float | int]:
    """값 목록의 개수, 합계와 평균을 계산합니다."""

    if not values:
        return {"count": 0, "total": 0, "average": 0.0}

    total = sum(values)

    return {
        "count": len(values),
        "total": total,
        "average": total / len(values),
    }


async def run_pipeline() -> list[dict[str, object]]:
    """비동기 수집 후 성공 데이터를 프로세스 풀에서 계산합니다."""

    sources = [
        SourceConfig("서울", 0.3, [100, 200, 300]),
        SourceConfig("부산", 0.1, [400, 500]),
        SourceConfig("대전", 0.2, [], should_fail=True),
    ]

    collected = await asyncio.gather(
        *(collect_source(source) for source in sources)
    )

    successful = [
        item
        for item in collected
        if item["status"] == "success"
    ]

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=2) as executor:
        calculation_tasks = [
            loop.run_in_executor(
                executor,
                calculate_statistics,
                item["values"],
            )
            for item in successful
        ]

        statistics = await asyncio.gather(*calculation_tasks)

    return [
        {
            "name": item["name"],
            "statistics": result,
        }
        for item, result in zip(successful, statistics)
    ]


def main() -> None:
    """파이프라인을 실행하고 결과를 출력합니다."""

    results = asyncio.run(run_pipeline())

    for result in results:
        print(result)


if __name__ == "__main__":
    main()