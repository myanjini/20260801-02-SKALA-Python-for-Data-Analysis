"""조건문과 반복문으로 프로그램의 실행 흐름을 제어합니다."""


score = 85
attendance_rate = 90

# and는 두 조건이 모두 참일 때 True를 반환합니다.
if score >= 80 and attendance_rate >= 80:
    print("수료 조건을 충족했습니다.")
else:
    print("수료 조건을 충족하지 못했습니다.")


# 점수 구간에 따라 등급을 결정합니다.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print("등급:", grade)


scores = [95, 62, 88, 0, 73]

# for문은 리스트의 값을 하나씩 순회합니다.
for current_score in scores:
    # 0점은 결시로 판단하고 다음 반복으로 이동합니다.
    if current_score == 0:
        print("결시 데이터는 제외합니다.")
        continue

    print(f"처리 점수: {current_score}")


count = 1

# while문은 조건이 True인 동안 반복합니다.
while count <= 3:
    print(f"{count}번째 반복입니다.")
    count += 1


# break는 조건을 만족하면 반복문을 즉시 종료합니다.
for number in range(1, 11):
    if number == 5:
        print("5를 발견하여 반복을 종료합니다.")
        break

    print("현재 숫자:", number)