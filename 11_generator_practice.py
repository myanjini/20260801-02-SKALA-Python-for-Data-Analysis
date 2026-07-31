# 제너레이터와 메모리 비교 실습
import sys

# 1. 리스트 컴프리헨션 (전체 생성 후 메모리 할당)
list_data = [x ** 2 for x in range(100000)]

# 2. 제너레이터 표현식 (지연 평가)
gen_data = (x ** 2 for x in range(100000))

print(f"리스트 메모리 사용량: {sys.getsizeof(list_data)} 바이트")
print(f"제너레이터 메모리 사용량: {sys.getsizeof(gen_data)} 바이트")

# 3. 제너레이터 함수 정의
def Stream_data_generator(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

stream = Stream_data_generator(3)
for val in stream:
    print(f"수신 데이터: {val}")