"""텍스트 파일을 쓰고 읽는 방법을 확인하는 예제입니다."""

from pathlib import Path  # 운영체제에 독립적인 경로 처리를 제공합니다.


# 실행 파일과 같은 위치에 생성할 파일 경로입니다.
file_path = Path("scores.txt")


# "w" 모드는 새 파일을 만들거나 기존 파일 내용을 덮어씁니다.
with file_path.open("w", encoding="utf-8") as file:
    # write()는 문자열을 파일에 기록합니다.
    file.write("김민수,90\n")
    file.write("이서연,85\n")


# "a" 모드는 기존 파일 내용 뒤에 새로운 내용을 추가합니다.
with file_path.open("a", encoding="utf-8") as file:
    file.write("박지훈,95\n")


# read()는 파일 전체 내용을 하나의 문자열로 반환합니다.
with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

print("[파일 전체 내용]")
print(content)


# 파일 객체를 반복하면 한 줄씩 읽을 수 있습니다.
with file_path.open("r", encoding="utf-8") as file:
    print("[학생별 점수]")

    for line in file:
        # strip()은 줄바꿈 문자를 제거합니다.
        clean_line = line.strip()

        # split(",")은 쉼표를 기준으로 문자열을 나눕니다.
        name, score = clean_line.split(",")

        # score는 문자열이므로 int()를 사용하여 정수로 변환합니다.
        print(f"{name}: {int(score)}점")


# exists()는 파일이 실제로 존재하는지 확인합니다.
print("파일 존재 여부:", file_path.exists())