"""Semaphore로 동시에 실행하는 작업 수를 제한합니다."""

import asyncio


async def limited_task(
    task_id: int,
    semaphore: asyncio.Semaphore,
) -> int:
    """세마포어를 획득한 동안에만 작업을 실행합니다."""

    async with semaphore:
        print(f"작업{task_id} 시작")
        await asyncio.sleep(0.1)
        print(f"작업{task_id} 완료")
        return task_id


async def main() -> None:
    """최대 두 작업만 동시에 실행합니다."""

    semaphore = asyncio.Semaphore(2)

    results = await asyncio.gather(
        *(limited_task(task_id, semaphore) for task_id in range(1, 6))
    )

    print("결과:", results)


if __name__ == "__main__":
    asyncio.run(main())