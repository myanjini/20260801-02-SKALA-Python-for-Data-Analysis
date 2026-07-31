# 1. 함수 정의
def divide_numbers(a, b):
    """두 숫자를 나누는 함수입니다."""
    # 2. 예외 처리 적용
    try:
        result = a / b
    except ZeroDivisionError:
        return "에러: 0으로 나눌 수 없습니다."
    except TypeError:
        return "에러: 숫자만 입력해 주세요."
    else:
        return f"계산 결과는 {result} 입니다."

# 함수 호출 및 결과 확인
print(divide_numbers(10, 2))
print(divide_numbers(10, 0)) # 예외 처리 발동
print(divide_numbers(10, "가나다")) # 예외 처리 발동