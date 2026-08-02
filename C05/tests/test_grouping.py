"""픽스처를 이용하여 지역별 매출 집계를 검증합니다."""


def group_total(records: list[dict[str, int | str]]) -> dict[str, int]:
    """지역별 매출 합계를 반환합니다."""

    result: dict[str, int] = {}

    for record in records:
        region = str(record["region"])
        amount = int(record["amount"])
        result[region] = result.get(region, 0) + amount

    return result


def test_group_total(sales_records) -> None:
    """지역별 합계 결과를 검증합니다."""

    assert group_total(sales_records) == {
        "서울": 4000,
        "부산": 2000,
    }


def test_fixture_is_independent(sales_records) -> None:
    """각 테스트에 새로운 리스트가 제공되는지 검증합니다."""

    sales_records.append({"region": "대전", "amount": 500})
    assert len(sales_records) == 4