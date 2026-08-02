"""람다 함수로 정렬, 변환과 필터링을 수행합니다."""


students = [
    {"name": "철수", "score": 90},
    {"name": "영희", "score": 80},
    {"name": "민수", "score": 95},
]

# score 값을 기준으로 내림차순 정렬합니다.
sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True,
)

# 90점 이상인 학생만 선택합니다.
high_students = list(
    filter(lambda student: student["score"] >= 90, students)
)

# 각 학생의 이름만 추출합니다.
high_student_names = list(
    map(lambda student: student["name"], high_students)
)

print("점수 내림차순:", sorted_students)
print("90점 이상:", high_student_names)