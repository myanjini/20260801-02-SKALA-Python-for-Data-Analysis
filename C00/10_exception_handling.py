"""사용자 입력을 안전하게 처리하는 예제입니다."""


def validate_score(score):
    """점수가 유효한 범위인지 검사합니다."""

    if not 0 <= score <= 100:
        # raise는 개발자가 의도적으로 예외를 발생시킬 때 사용합니다.
        raise ValueError("점수는 0부터 100 사이여야 합니다.")

    return score


def read_score():
    """사용자에게 점수를 입력받아 검증한 결과를 반환합니다."""

    try:
        # input()의 결과는 문자열이므로 int()로 변환합니다.
        raw_value = input("점수를 입력하세요: ")
        score = int(raw_value)

        # 점수 범위를 검증합니다.
        return validate_score(score)

    except ValueError as error:
        # 숫자 변환 오류와 점수 범위 오류를 처리합니다.
        print("입력 오류:", error)
        return None

    finally:
        # 예외 발생 여부와 관계없이 항상 실행합니다.
        print("입력 처리를 완료했습니다.")


score = read_score()

if score is not None:
    print(f"등록된 점수는 {score}점입니다.")
else:
    print("점수를 등록하지 않았습니다.")