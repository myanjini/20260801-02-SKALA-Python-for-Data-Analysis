"""기본 타입 힌트의 작성 방법을 확인합니다."""


# 변수에 예상 타입을 표시합니다.
course_name: str = "데이터 분석"
student_count: int = 30
average_score: float = 87.5
is_active: bool = True


def calculate_total(price: int, quantity: int) -> int:
    """가격과 수량을 곱한 총금액을 반환합니다."""

    return price * quantity


def format_summary(name: str, total: int) -> str:
    """이름과 총금액을 문자열로 반환합니다."""

    return f"{name}:{total:,}원"


total_amount: int = calculate_total(15_000, 3)
summary: str = format_summary(course_name, total_amount)

print(summary)
print("학생 수:", student_count)
print("평균 점수:", average_score)
print("활성 상태:", is_active)