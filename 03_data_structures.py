# 1. 리스트 (추가 및 수정 가능)
fruits = ["사과", "바나나", "포도"]
fruits.append("오렌지") # 추가
fruits[0] = "수박"      # 수정
print("리스트:", fruits)

# 2. 튜플 (수정 불가)
colors = ("빨강", "파랑", "노랑")
print("\n튜플:", colors)
# colors[0] = "검정" # 주석을 해제하고 실행하면 에러가 발생합니다.

# 3. 딕셔너리 (키-값 쌍)
employee = {"이름": "홍길동", "부서": "데이터팀", "나이": 30}
employee["직급"] = "대리" # 새로운 데이터 추가
print("\n딕셔너리:", employee)
print("부서 확인:", employee["부서"])

# 4. 집합 (중복 제거)
numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print("\n집합(중복제거):", numbers)