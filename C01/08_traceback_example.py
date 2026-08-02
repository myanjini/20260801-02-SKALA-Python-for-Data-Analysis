"""함수 호출 과정에서 발생한 오류 추적 정보를 확인합니다."""

import traceback  # 예외의 전체 호출 경로를 출력합니다.


def divide(total, count):
    """합계를 개수로 나누어 평균을 반환합니다."""

    return total / count


def calculate_average(scores):
    """점수 리스트의 평균을 계산합니다."""

    return divide(sum(scores), len(scores))


def create_report(scores):
    """점수 평균을 포함한 보고서를 생성합니다."""

    average = calculate_average(scores)
    return f"평균 점수:{average:.1f}"


try:
    # 빈 리스트의 길이는 0이므로 예외가 발생합니다.
    print(create_report([]))

except ZeroDivisionError:
    print("평균 계산 중 오류가 발생했습니다.")
    traceback.print_exc()