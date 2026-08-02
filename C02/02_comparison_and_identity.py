"""==와 is의 차이를 확인합니다."""


# 내용은 같지만 서로 독립적으로 생성한 리스트입니다.
list_a = [1, 2, 3]
list_b = [1, 2, 3]

# list_c는 list_a와 같은 객체를 참조합니다.
list_c = list_a

# ==는 저장된 값의 같음을 비교합니다.
print("A와 B의 값 동일성:", list_a == list_b)

# is는 동일한 객체를 참조하는지 비교합니다.
print("A와 B의 객체 동일성:", list_a is list_b)
print("A와 C의 객체 동일성:", list_a is list_c)

result = None

# None은 is None으로 확인합니다.
print("결과 없음:", result is None)

allowed_regions = {"서울", "부산", "대전"}
current_region = "서울"

# in은 값이 집합에 포함되어 있는지 확인합니다.
print("서비스 가능 지역:", current_region in allowed_regions)