"""zip과 zip_longest의 차이를 확인합니다."""

from itertools import zip_longest


names = ["Alice", "Bob", "Charlie"]
scores = [90, 85]

# zip()은 가장 짧은 데이터의 길이에 맞추어 종료합니다.
zipped_result = list(zip(names, scores))

# zip_longest()는 가장 긴 데이터의 길이에 맞추어 결합합니다.
longest_result = list(
    zip_longest(names, scores, fillvalue="정보 없음")
)

print("zip 결과:", zipped_result)
print("zip_longest 결과:", longest_result)


keys = ["name", "age", "city"]
values = ["Alice", 25]

# 누락된 값은 지정한 기본값으로 채웁니다.
person = dict(zip_longest(keys, values, fillvalue="정보 없음"))
print("사용자 정보:", person)