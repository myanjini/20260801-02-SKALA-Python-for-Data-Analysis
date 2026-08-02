"""성적 처리 기능을 여러 함수로 분리하는 예제입니다."""


def calculate_average(scores):
    """점수 리스트를 받아 평균을 반환합니다."""

    # 빈 리스트가 전달되면 나눗셈 오류를 막기 위해 0.0을 반환합니다.
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def determine_grade(average):
    """평균 점수를 받아 등급을 반환합니다."""

    if average >= 90:
        return "A"

    if average >= 80:
        return "B"

    if average >= 70:
        return "C"

    return "D"


def create_report(name, scores, title="성적 보고서"):
    """학생 이름과 점수로 보고서 문자열을 생성합니다."""

    average = calculate_average(scores)
    grade = determine_grade(average)

    return (
        f"[{title}]\n"
        f"학생: {name}\n"
        f"점수: {scores}\n"
        f"평균: {average:.1f}\n"
        f"등급: {grade}"
    )


# 함수 호출에 사용할 변수입니다.
student_name = "김민수"
student_scores = [90, 85, 95]

# create_report()의 반환값을 report 변수에 저장합니다.
report = create_report(student_name, student_scores)

print(report)