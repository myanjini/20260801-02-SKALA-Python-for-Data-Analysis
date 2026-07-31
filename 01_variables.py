# 1. 다양한 타입의 변수 선언
age = 25              # 정수형 변수
name = "데이터분석가"   # 문자열 변수
is_student = False    # 불리언 변수

print("이름:", name)
print("나이:", age)
print("학생 여부:", is_student)

# 2. 파이썬 예약어 확인 (이 단어들은 변수명으로 쓸 수 없습니다)
import keyword
print("\n파이썬 예약어 목록:")
print(keyword.kwlist)
