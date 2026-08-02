"""문자열 생성과 처리 방법을 확인하는 예제입니다."""

course = "Python 데이터 분석"

# len() 함수는 문자열의 전체 문자 수를 반환합니다.
print("문자 수:", len(course))

# 문자열의 특정 위치에 접근합니다.
print("첫 번째 문자:", course[0])
print("마지막 문자:", course[-1])

# 문자열의 일부 범위를 추출합니다.
print("0번부터 5번 앞까지:", course[0:6])
print("6번부터 끝까지:", course[6:])
print("문자열 뒤집기:", course[::-1])

first_name = "길동"
last_name = "홍"

# + 연산자는 문자열을 연결합니다.
full_name = last_name + first_name
print("이름:", full_name)

# * 연산자는 문자열을 반복합니다.
print("-" * 20)

score = 95

# f-string은 문자열 안에 변수나 계산식을 삽입합니다.
print(f"{full_name}님의 점수는 {score}점입니다.")

raw_text = "  Data Analysis  "

# strip()은 문자열 양쪽의 공백을 제거합니다.
clean_text = raw_text.strip()

# lower()는 영문자를 소문자로 변환합니다.
print("공백 제거:", clean_text)
print("소문자 변환:", clean_text.lower())

# replace()는 지정한 문자열을 다른 문자열로 치환한 새 값을 반환합니다.
print("문자열 치환:", clean_text.replace("Data", "Python"))
