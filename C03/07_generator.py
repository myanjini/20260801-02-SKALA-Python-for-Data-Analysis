"""제너레이터로 입력 행을 하나씩 변환합니다."""


def parse_numbers(lines):
    """빈 행을 제외하고 정수값을 하나씩 생성합니다."""

    for line_number, line in enumerate(lines, start=1):
        clean_line = line.strip()

        if not clean_line:
            continue

        try:
            value = int(clean_line)
        except ValueError:
            print(f"{line_number}행 제외:{clean_line}")
            continue

        yield value


raw_lines = ["10\n", "20\n", "\n", "오류\n", "30\n"]
number_generator = parse_numbers(raw_lines)

print("제너레이터 타입:", type(number_generator).__name__)

for number in number_generator:
    print("숫자:", number)