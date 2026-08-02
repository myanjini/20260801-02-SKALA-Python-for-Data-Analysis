"""timeit과 cProfile로 코드 성능을 측정합니다."""

import cProfile
import io
import pstats
import timeit


def sum_with_loop(limit: int) -> int:
    """일반 반복문으로 정수 합계를 계산합니다."""

    total = 0

    for number in range(limit):
        total += number

    return total


def sum_with_builtin(limit: int) -> int:
    """내장 sum()으로 정수 합계를 계산합니다."""

    return sum(range(limit))


loop_time = timeit.timeit(
    lambda: sum_with_loop(100_000),
    number=10,
)

builtin_time = timeit.timeit(
    lambda: sum_with_builtin(100_000),
    number=10,
)

print(f"반복문 시간:{loop_time:.6f}초")
print(f"내장 함수 시간:{builtin_time:.6f}초")


profiler = cProfile.Profile()
profiler.enable()
sum_with_loop(100_000)
profiler.disable()

stream = io.StringIO()
statistics = pstats.Stats(profiler, stream=stream)
statistics.sort_stats("cumulative").print_stats(5)

print(stream.getvalue())