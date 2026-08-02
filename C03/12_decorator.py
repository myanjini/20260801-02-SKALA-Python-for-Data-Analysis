"""데코레이터로 함수 실행 시간을 측정합니다."""

import time
from functools import wraps


def timer(function):
    """대상 함수의 실행 시간을 출력하는 데코레이터입니다."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        """대상 함수를 호출하고 실행 시간을 계산합니다."""

        start_time = time.perf_counter()

        # 원래 함수의 결과를 보존합니다.
        result = function(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time
        print(f"{function.__name__} 실행 시간:{elapsed_time:.6f}초")

        return result

    return wrapper


@timer
def calculate_total(numbers):
    """숫자 목록의 합계를 반환합니다."""

    return sum(numbers)


result = calculate_total(range(1, 1001))

print("합계:", result)
print("함수 이름:", calculate_total.__name__)
print("함수 설명:", calculate_total.__doc__)