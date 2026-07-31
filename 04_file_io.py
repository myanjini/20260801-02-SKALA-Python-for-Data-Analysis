# 1. 파일 쓰기 ('w' 모드는 기존 내용을 덮어씁니다)
with open('sample_data.txt', 'w', encoding='utf-8') as f:
    f.write("첫 번째 줄입니다.\n")
    f.write("두 번째 줄입니다.\n")

# 2. 파일에 내용 추가하기 ('a' 모드는 기존 내용 뒤에 추가합니다)
with open('sample_data.txt', 'a', encoding='utf-8') as f:
    f.write("세 번째 줄이 추가되었습니다.\n")

# 3. 파일 읽기 ('r' 모드)
print("--- 파일 내용 출력 ---")
with open('sample_data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines() # 모든 줄을 리스트 형태로 읽어옵니다.
    for line in lines:
        print(line.strip()) # strip()을 사용하여 줄바꿈 문자를 제거합니다.