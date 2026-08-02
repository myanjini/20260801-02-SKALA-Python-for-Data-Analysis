"""숫자 데이터와 산술 연산자를 확인하는 예제입니다."""

# 두 개의 정수형 변수입니다.
number_a = 10
number_b = 3

# 기본 산술 연산입니다.
print("덧셈:", number_a + number_b)
print("뺄셈:", number_a - number_b)
print("곱셈:", number_a * number_b)
print("나눗셈:", number_a / number_b)
print("몫:", number_a // number_b)
print("나머지:", number_a % number_b)
print("거듭제곱:", number_a**number_b)

# 정수와 실수를 함께 계산하면 결과가 실수로 변환됩니다.
mixed_result = number_a + 2.5
print("혼합 연산:", mixed_result)
print("혼합 연산 타입:", type(mixed_result))

# int() 함수는 값을 정수로 변환합니다.
integer_value = int(3.9)

# float() 함수는 값을 실수로 변환합니다.
float_value = float(7)

print("정수 변환:", integer_value)
print("실수 변환:", float_value)

# 괄호를 사용하여 연산 순서를 명확하게 지정합니다.
score_1 = 80
score_2 = 90
score_3 = 100
average = (score_1 + score_2 + score_3) / 3

print("평균:", average)
