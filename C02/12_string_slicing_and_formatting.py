"""문자열 슬라이싱과 f-string 포매팅을 사용합니다."""


text = "Hello, Python!"

print("첫 단어:", text[0:5])
print("두 번째 단어:", text[7:13])
print("마지막 문자:", text[-1])
print("역순:", text[::-1])


name = "Alice"
amount = 1234567
average = 87.456

# 쉼표는 천 단위 구분 기호를 표시합니다.
print(f"담당자:{name}")
print(f"매출액:{amount:,}원")

# .2f는 실수를 소수점 둘째 자리까지 출력합니다.
print(f"평균 점수:{average:.2f}")

# 중괄호 안에서 간단한 표현식을 계산할 수 있습니다.
print(f"부가세 포함 금액:{amount * 1.1:,.0f}원")