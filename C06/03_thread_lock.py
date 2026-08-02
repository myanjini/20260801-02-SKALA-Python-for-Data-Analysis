"""Lock으로 공유 카운터의 변경을 보호합니다."""

import threading


counter = 0
counter_lock = threading.Lock()


def increment_many(times: int) -> None:
    """공유 카운터를 지정된 횟수만큼 증가시킵니다."""

    global counter

    for _ in range(times):
        # with 블록을 벗어나면 잠금을 자동으로 해제합니다.
        with counter_lock:
            counter += 1


threads = [
    threading.Thread(target=increment_many, args=(10_000,))
    for _ in range(4)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("최종 카운터:", counter)