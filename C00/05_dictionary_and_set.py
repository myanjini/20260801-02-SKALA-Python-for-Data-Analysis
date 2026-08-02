"""딕셔너리와 집합의 주요 기능을 확인하는 예제입니다."""

# 학생 한 명의 정보를 키와 값의 쌍으로 저장합니다.
student = {
    "name": "김민수",
    "age": 20,
    "score": 95,
}

# 키를 사용하여 값을 조회합니다.
print("이름:", student["name"])

# 기존 키의 값을 수정합니다.
student["score"] = 98

# 새로운 키와 값을 추가합니다.
student["city"] = "서울"

# get()은 키가 없을 때 지정한 기본값을 반환합니다.
print("전공:", student.get("major", "정보 없음"))

# items()는 키와 값을 함께 반복할 때 사용합니다.
for key, value in student.items():
    print(f"{key}: {value}")


# 중복된 지역명을 포함한 리스트입니다.
region_list = ["서울", "부산", "서울", "대전", "부산"]

# set()은 중복을 제거한 집합을 생성합니다.
unique_regions = set(region_list)

# 집합은 출력 순서를 보장하지 않습니다.
print("중복 제거 지역:", unique_regions)

team_a = {"Python", "Pandas", "SQL"}
team_b = {"Python", "Java", "SQL"}

# | 연산자는 합집합을 반환합니다.
print("전체 기술:", team_a | team_b)

# & 연산자는 교집합을 반환합니다.
print("공통 기술:", team_a & team_b)

# - 연산자는 차집합을 반환합니다.
print("A팀만 보유:", team_a - team_b)
