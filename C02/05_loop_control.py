"""break, continue, else를 사용하여 데이터를 검색합니다."""


scores = [85, None, 72, 95, 61]
target_score = 95

for score in scores:
    # 결측값은 계산하지 않고 다음 반복으로 이동합니다.
    if score is None:
        print("결측값을 제외합니다.")
        continue

    print("확인 점수:", score)

    # 목표 점수를 찾으면 반복문을 즉시 종료합니다.
    if score == target_score:
        print("목표 점수를 찾았습니다.")
        break

else:
    # break가 실행되지 않았을 때만 실행합니다.
    print("목표 점수를 찾지 못했습니다.")