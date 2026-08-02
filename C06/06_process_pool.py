"""ProcessPoolExecutor로 여러 계산 작업을 병렬 실행합니다."""

from concurrent.futures import ProcessPoolExecutor


def sum_of_squares(limit: int) -> int:
    """0부터 limit 직전까지 제곱의 합을 반환합니다."""

    return sum(number * number for number in range(limit))


def main() -> None:
    """여러 입력을 프로세스 풀에서 계산합니다."""

    limits = [10_000, 20_000, 30_000]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(sum_of_squares, limits))

    for limit, result in zip(limits, results):
        print(f"{limit}:{result}")


if __name__ == "__main__":
    main()