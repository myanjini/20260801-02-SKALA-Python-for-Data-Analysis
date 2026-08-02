"""ThreadPoolExecutor로 여러 입출력 작업의 결과를 수집합니다."""

import time
from concurrent.futures import Future, ThreadPoolExecutor, as_completed


def load_resource(resource_id: int) -> str:
    """외부 자원 읽기를 대기 시간으로 모의합니다."""

    time.sleep(0.05 * resource_id)

    if resource_id == 3:
        raise OSError("3번 자원을 읽지 못했습니다.")

    return f"자원{resource_id}"


with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_id: dict[Future[str], int] = {
        executor.submit(load_resource, resource_id): resource_id
        for resource_id in range(1, 5)
    }

    for future in as_completed(future_to_id):
        resource_id = future_to_id[future]

        try:
            result = future.result()
        except OSError as error:
            print(f"{resource_id}번 실패:{error}")
        else:
            print(f"{resource_id}번 성공:{result}")