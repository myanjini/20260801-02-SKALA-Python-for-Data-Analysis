"""asyncio로 여러 대기 작업을 동시에 진행합니다."""

import asyncio
import time


async def fetch_data(source: str, delay: float) -> str:
    """비동기 데이터 요청을 sleep으로 모의합니다."""

    print(f"{source} 요청 시작")

    # time.sleep()과 달리 이벤트 루프에 제어권을 양보합니다.
    await asyncio.sleep(delay)

    print(f"{source} 요청 완료")
    return f"{source} 데이터"


async def main() -> None:
    """여러 코루틴을 동시에 실행하고 결과를 출력합니다."""

    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_data("날씨", 0.3),
        fetch_data("환율", 0.1),
        fetch_data("뉴스", 0.2),
    )

    elapsed = time.perf_counter() - start

    print("결과:", results)
    print(f"실행 시간:{elapsed:.2f}초")


if __name__ == "__main__":
    asyncio.run(main())