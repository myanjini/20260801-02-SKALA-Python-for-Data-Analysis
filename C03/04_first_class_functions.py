"""함수를 객체로 저장하여 데이터 변환 파이프라인을 구성합니다."""


def strip_text(value):
    """문자열 양쪽의 공백을 제거합니다."""

    return value.strip()


def normalize_case(value):
    """문자열을 소문자로 변환합니다."""

    return value.lower()


def replace_spaces(value):
    """공백을 밑줄로 변경합니다."""

    return value.replace(" ", "_")


def apply_pipeline(value, functions):
    """전달받은 함수를 순서대로 적용합니다."""

    result = value

    for function in functions:
        result = function(result)

    return result


# 함수 객체를 리스트에 저장합니다.
pipeline = [strip_text, normalize_case, replace_spaces]

raw_text = "  Data Analysis  "
clean_text = apply_pipeline(raw_text, pipeline)

print("원본:", repr(raw_text))
print("변환:", clean_text)