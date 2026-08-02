"""threading 모듈로 여러 작업을 동시에 진행합니다."""

import threading
import time


def worker(worker_id: int, delay: float) -> None:
    """지정한 시간만큼 기다린 후 완료 메시지를 출력합니다."""

    print(f"작업{worker_id} 시작")
    time.sleep(delay)
    print(f"작업{worker_id} 완료")


threads: list[threading.Thread] = []

for worker_id, delay in [(1, 0.3), (2, 0.1), (3, 0.2)]:
    thread = threading.Thread(
        target=worker,
        args=(worker_id, delay),
        name=f"worker-{worker_id}",
    )
    threads.append(thread)
    thread.start()

# 모든 스레드가 끝날 때까지 메인 스레드가 기다립니다.
for thread in threads:
    thread.join()

print("모든 작업 완료")