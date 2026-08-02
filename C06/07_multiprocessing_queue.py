"""multiprocessing.Queue로 자식 프로세스의 결과를 수집합니다."""

import multiprocessing as mp


def worker(task_id: int, value: int, result_queue: mp.Queue) -> None:
    """입력값의 제곱을 계산하여 결과 큐에 넣습니다."""

    result_queue.put(
        {
            "task_id": task_id,
            "result": value * value,
        }
    )


def main() -> None:
    """작업 프로세스를 실행하고 큐에서 결과를 수집합니다."""

    result_queue = mp.Queue()
    processes = [
        mp.Process(target=worker, args=(1, 10, result_queue)),
        mp.Process(target=worker, args=(2, 20, result_queue)),
    ]

    for process in processes:
        process.start()

    results = [result_queue.get() for _ in processes]

    for process in processes:
        process.join()

    # 큐 도착 순서는 달라질 수 있으므로 작업 ID로 정렬합니다.
    results.sort(key=lambda item: item["task_id"])
    print(results)


if __name__ == "__main__":
    main()