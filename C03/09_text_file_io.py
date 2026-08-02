"""pathlib과 with문으로 텍스트 파일을 안전하게 처리합니다."""

from pathlib import Path


# 현재 경로 아래의 output 디렉터리를 나타냅니다.
output_directory = Path("output")

# parents=True는 상위 경로도 생성하며 exist_ok=True는 기존 경로를 허용합니다.
output_directory.mkdir(parents=True, exist_ok=True)

file_path = output_directory / "sales_report.txt"

report_lines = [
    "서울,150000",
    "부산,120000",
    "대전,90000",
]

# with 블록이 끝나면 파일을 자동으로 닫습니다.
with file_path.open("w", encoding="utf-8") as file:
    for line in report_lines:
        file.write(line + "\n")

print("파일 존재:", file_path.exists())

with file_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        # strip()은 줄바꿈 문자를 제거합니다.
        print(f"{line_number}행:", line.strip())