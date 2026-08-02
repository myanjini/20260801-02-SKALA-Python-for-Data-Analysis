"""리스트·딕셔너리·집합 컴프리헨션을 사용합니다."""


numbers = range(1, 11)

# 짝수의 제곱값만 리스트로 생성합니다.
even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

# 숫자를 키, 홀짝 정보를 값으로 저장합니다.
number_types = {
    number: "짝수" if number % 2 == 0 else "홀수"
    for number in numbers
}

words = ["python", "data", "python", "analysis"]

# 단어 길이의 중복 없는 집합을 생성합니다.
word_lengths = {len(word) for word in words}

print("짝수 제곱:", even_squares)
print("1의 분류:", number_types[1])
print("2의 분류:", number_types[2])
print("단어 길이 집합:", word_lengths)