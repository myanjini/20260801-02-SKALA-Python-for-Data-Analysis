"""multiprocessing.Process로 계산 작업을 실행합니다."""

import multiprocessing as mp
import os


def calculate_sum(limit: int) -> None:
    """0부터 limit 직전까지 제곱의 합을 계산하여 출력합니다."""

    result = sum(number * number for number in range(limit))
    print(f"프로세스{os.getpid()} 결과:{result}")


def main() -> None:
    """두 계산 프로세스를 생성하고 종료를 기다립니다."""

    processes = [
        mp.Process(target=calculate_sum, args=(10_000,)),
        mp.Process(target=calculate_sum, args=(20_000,)),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("모든 프로세스 완료")


if __name__ == "__main__":
    main()