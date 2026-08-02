"""순차 실행과 스레드 기반 동시 실행 시간을 비교합니다."""

import time
from concurrent.futures import ThreadPoolExecutor


def waiting_task(task_id: int, delay: float = 0.2) -> str:
    """외부 입출력을 기다리는 상황을 sleep으로 모의합니다."""

    time.sleep(delay)
    return f"작업{task_id} 완료"


def run_sequentially(task_count: int) -> list[str]:
    """작업을 하나씩 순차적으로 실행합니다."""

    return [waiting_task(task_id) for task_id in range(task_count)]


def run_concurrently(task_count: int) -> list[str]:
    """스레드 풀에서 여러 대기 작업을 함께 진행합니다."""

    with ThreadPoolExecutor(max_workers=task_count) as executor:
        return list(executor.map(waiting_task, range(task_count)))


task_count = 4

start = time.perf_counter()
sequential_results = run_sequentially(task_count)
sequential_time = time.perf_counter() - start

start = time.perf_counter()
concurrent_results = run_concurrently(task_count)
concurrent_time = time.perf_counter() - start

print("순차 결과:", sequential_results)
print("동시 결과:", concurrent_results)
print(f"순차 시간:{sequential_time:.2f}초")
print(f"동시 시간:{concurrent_time:.2f}초")