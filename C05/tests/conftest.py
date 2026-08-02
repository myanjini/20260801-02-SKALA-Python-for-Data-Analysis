"""여러 테스트가 공유하는 픽스처를 정의합니다."""

import pytest


@pytest.fixture
def sales_records() -> list[dict[str, int | str]]:
    """테스트마다 새로운 매출 레코드 목록을 반환합니다."""

    return [
        {"region": "서울", "amount": 1000},
        {"region": "부산", "amount": 2000},
        {"region": "서울", "amount": 3000},
    ]