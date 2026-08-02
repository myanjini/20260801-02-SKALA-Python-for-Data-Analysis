"""단락 평가의 실행 순서와 기본값 처리를 확인합니다."""


def left_check():
    """왼쪽 조건의 실행 여부를 출력하고 False를 반환합니다."""

    print("왼쪽 조건을 검사합니다.")
    return False


def right_check():
    """오른쪽 조건의 실행 여부를 출력하고 True를 반환합니다."""

    print("오른쪽 조건을 검사합니다.")
    return True


# 왼쪽이 False이므로 right_check()는 실행하지 않습니다.
result = left_check() and right_check()
print("and 결과:", result)

# 빈 문자열은 거짓이므로 오른쪽 기본값을 선택합니다.
configured_name = ""
display_name = configured_name or "이름 없음"
print("표시 이름:", display_name)

# 빈 리스트가 반환된다는 점을 확인합니다.
print("원래 값 반환:", [] and [1])