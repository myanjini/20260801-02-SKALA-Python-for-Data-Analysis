"""함수의 바이트코드를 dis 모듈로 확인합니다."""

import dis  # 코드 객체의 바이트코드를 분석합니다.


def add(number_a, number_b):
    """두 숫자를 더한 결과를 반환합니다."""

    return number_a + number_b


def determine_status(score):
    """점수에 따라 합격 또는 불합격을 반환합니다."""

    if score >= 80:
        return "합격"

    return "불합격"


print("[add 함수의 바이트코드]")
dis.dis(add)

print("\n[determine_status 함수의 바이트코드]")
dis.dis(determine_status)

print("\n[함수 실행 결과]")
print("10 + 20 =", add(10, 20))
print("85점 판정:", determine_status(85))