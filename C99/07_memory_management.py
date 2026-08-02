import gc
import sys

# 1. 참조 카운트 확인 [교안 30페이지]
data_list = [1, 2, 3, 4, 5]
print(f"초기 참조 카운트: {sys.getrefcount(data_list) - 1}")

ref_copy = data_list
print(f"참조 추가 후 카운트: {sys.getrefcount(data_list) - 1}")

del ref_copy
print(f"참조 삭제 후 카운트: {sys.getrefcount(data_list) - 1}")


# 2. 순환 참조 및 가비지 컬렉터 수동 작동 [교안 29페이지]
class Node:

    def __init__(self, value):
        self.value = value
        self.self_ref = None


node1 = Node("A")
node2 = Node("B")

# 순환 참조 발생
node1.self_ref = node2
node2.self_ref = node1

del node1
del node2

# 수동 가비지 컬렉션 수행 [교안 29페이지]
collected = gc.collect()
print(f"가비지 컬렉터에 의해 해제된 객체 수: {collected}")