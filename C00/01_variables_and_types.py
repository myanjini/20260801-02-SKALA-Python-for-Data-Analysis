"""변수와 기본 데이터 타입을 확인하는 예제입니다."""

import keyword  # Python 예약어 정보를 제공하는 표준 모듈입니다.


# 정수형 변수입니다.
student_count = 30

# 실수형 변수입니다.
average_score = 87.5

# 문자열 변수입니다.
course_name = "데이터 분석"

# 불리언 변수입니다.
is_completed = False

# 값이 없음을 나타내는 변수입니다.
result = None


# type() 함수는 전달받은 값이나 변수의 데이터 타입을 반환합니다.
print("학생 수:", student_count, type(student_count))
print("평균 점수:", average_score, type(average_score))
print("과정명:", course_name, type(course_name))
print("수료 여부:", is_completed, type(is_completed))
print("결과:", result, type(result))

# keyword.iskeyword() 함수는 문자열이 예약어인지 확인합니다.
print("if는 예약어입니까?", keyword.iskeyword("if"))
print("student는 예약어입니까?", keyword.iskeyword("student"))

# keyword.kwlist에는 Python의 전체 예약어가 저장됩니다.
print("예약어 개수:", len(keyword.kwlist))