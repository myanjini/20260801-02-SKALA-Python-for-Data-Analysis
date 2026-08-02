"""가변 인자와 인자 언패킹을 이용하여 데이터를 집계합니다."""


def aggregate(*values, **options):
    """여러 숫자를 지정한 방식으로 집계합니다."""

    operation = options.get("operation", "sum")
    label = options.get("label", "결과")

    if operation == "sum":
        result = sum(values)
    elif operation == "average":
        result = sum(values) / len(values) if values else 0
    else:
        raise ValueError(f"지원하지 않는 연산:{operation}")

    return f"{label}:{result}"


numbers = [10, 20, 30]
settings = {
    "operation": "average",
    "label": "평균",
}

# *는 리스트의 요소를 위치 인자로 펼칩니다.
# **는 딕셔너리의 항목을 키워드 인자로 펼칩니다.
print(aggregate(*numbers, **settings))

print(aggregate(1, 2, 3, 4, label="합계"))