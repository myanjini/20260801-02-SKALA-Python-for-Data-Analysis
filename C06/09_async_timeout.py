"""비동기 작업에 시간 제한을 적용합니다."""

import asyncio


async def slow_operation(name: str, delay: float) -> str:
    """지정된 시간 뒤에 작업 결과를 반환합니다."""

    await asyncio.sleep(delay)
    return f"{name} 완료"


async def run_with_timeout(
    name: str,
    delay: float,
    timeout_seconds: float,
) -> str:
    """작업을 제한 시간 안에 실행하고 결과 메시지를 반환합니다."""

    try:
        return await asyncio.wait_for(
            slow_operation(name, delay),
            timeout=timeout_seconds,
        )
    except TimeoutError:
        return f"{name} 시간 초과"


async def main() -> None:
    """성공 작업과 시간 초과 작업을 함께 실행합니다."""

    results = await asyncio.gather(
        run_with_timeout("빠른 작업", 0.1, 0.2),
        run_with_timeout("느린 작업", 0.3, 0.2),
    )

    print(results)


if __name__ == "__main__":
    asyncio.run(main())