"""리스트, 튜플, 집합과 딕셔너리의 특성을 비교합니다."""


# 리스트는 생성 후 요소를 변경할 수 있습니다.
scores = [90, 80, 90]
scores.append(100)
scores[1] = 85

# 튜플은 생성 후 요소를 변경할 수 없습니다.
coordinate = (37.5665, 126.9780)

# 집합은 중복값을 제거합니다.
unique_scores = set(scores)

# 딕셔너리는 키와 값의 쌍을 저장합니다.
student = {
    "name": "김민수",
    "scores": scores,
}

student["average"] = sum(scores) / len(scores)

print("리스트:", scores)
print("튜플:", coordinate)
print("집합:", unique_scores)
print("딕셔너리:", student)
print("이름 키 존재:", "name" in student)