"""deque로 대기열과 고정 길이 최근 데이터를 관리합니다."""

from collections import deque


# 처리할 작업을 저장하는 대기열입니다.
task_queue = deque(["작업1", "작업2"])

# 오른쪽 끝에 새 작업을 추가합니다.
task_queue.append("작업3")

# 긴급 작업을 왼쪽 끝에 추가합니다.
task_queue.appendleft("긴급작업")

print("현재 대기열:", task_queue)

# 왼쪽 끝의 작업부터 처리합니다.
while task_queue:
    current_task = task_queue.popleft()
    print("처리:", current_task)


# maxlen은 저장할 수 있는 최대 요소 수입니다.
recent_values = deque(maxlen=3)

for value in [10, 20, 30, 40]:
    recent_values.append(value)
    print("최근 값:", list(recent_values))