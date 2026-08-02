"""문자열로 작성한 Python 코드의 문법을 검사합니다."""


def check_syntax(source_code, code_name):
    """소스코드를 컴파일하여 문법의 유효성을 검사합니다."""

    try:
        # "exec"는 여러 문장으로 구성된 코드를 검사하는 모드입니다.
        compile(source_code, code_name, "exec")

    except SyntaxError as error:
        # lineno는 문법 오류가 발생한 줄 번호입니다.
        print(f"[{code_name}] 문법 오류")
        print("오류 줄:", error.lineno)
        print("오류 내용:", error.msg)

    else:
        print(f"[{code_name}] 문법이 올바릅니다.")


valid_code = """
score = 90
if score >= 80:
    print("합격입니다.")
"""

invalid_code = """
score = 90
if score >= 80
    print("합격입니다.")
"""

check_syntax(valid_code, "valid_code")
check_syntax(invalid_code, "invalid_code")