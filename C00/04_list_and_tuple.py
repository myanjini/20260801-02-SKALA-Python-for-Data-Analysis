"""리스트와 튜플의 차이를 확인하는 예제입니다."""


# 학생 점수를 저장하는 리스트입니다.
scores = [85, 90, 75]

# append()는 리스트 마지막에 값을 추가합니다.
scores.append(95)

# insert()는 지정한 위치에 값을 삽입합니다.
scores.insert(1, 88)

# 인덱스를 사용하여 특정 값을 수정합니다.
scores[0] = 87

print("수정 후 점수:", scores)

# remove()는 전달받은 값과 같은 첫 번째 요소를 제거합니다.
scores.remove(75)

# sort()는 원본 리스트를 오름차순으로 정렬합니다.
scores.sort()

print("정렬 후 점수:", scores)
print("최고 점수:", scores[-1])

# 리스트 컴프리헨션으로 1부터 5까지의 제곱값을 생성합니다.
squares = [number ** 2 for number in range(1, 6)]
print("제곱 목록:", squares)

# 조건을 추가하여 짝수만 선택합니다.
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print("짝수 목록:", even_numbers)

# 위도와 경도를 변경할 수 없는 튜플로 저장합니다.
seoul_coordinate = (37.5665, 126.9780)

print("서울 위도:", seoul_coordinate[0])
print("서울 경도:", seoul_coordinate[1])

# 아래 코드를 실행하면 튜플은 수정할 수 없으므로 TypeError가 발생합니다.
# seoul_coordinate[0] = 38.0