"""heapq와 bisect를 이용하여 우선순위와 정렬 상태를 관리합니다."""

import bisect
import heapq


# 튜플의 첫 번째 값인 우선순위를 기준으로 최소 힙을 구성합니다.
task_heap = []

heapq.heappush(task_heap, (2, "보고서 작성"))
heapq.heappush(task_heap, (1, "장애 처리"))
heapq.heappush(task_heap, (3, "자료 정리"))

while task_heap:
    priority, task_name = heapq.heappop(task_heap)
    print(f"우선순위{priority}:{task_name}")


# 정렬된 점수 목록입니다.
sorted_scores = [60, 70, 80, 90]

# bisect_left()는 75가 들어갈 위치를 반환합니다.
position = bisect.bisect_left(sorted_scores, 75)
print("75의 삽입 위치:", position)

# insort()는 정렬 상태를 유지하면서 값을 삽입합니다.
bisect.insort(sorted_scores, 75)
print("삽입 후 점수:", sorted_scores)