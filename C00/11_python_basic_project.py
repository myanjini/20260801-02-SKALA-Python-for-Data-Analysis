"""Python 기초 문법을 종합적으로 활용하는 성적 관리 프로그램입니다."""

from pathlib import Path


class Student:
    """학생 한 명의 이름과 점수를 관리합니다."""

    def __init__(self, name):
        """학생 이름과 빈 점수 리스트를 초기화합니다."""

        self.name = name
        self.scores = []

    def add_score(self, score):
        """유효한 점수를 리스트에 추가합니다."""

        if not 0 <= score <= 100:
            raise ValueError("점수는 0부터 100 사이여야 합니다.")

        self.scores.append(score)

    def average(self):
        """점수 평균을 반환합니다."""

        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)

    def grade(self):
        """평균 점수에 따른 등급을 반환합니다."""

        average_score = self.average()

        if average_score >= 90:
            return "A"

        if average_score >= 80:
            return "B"

        if average_score >= 70:
            return "C"

        return "D"

    def to_dictionary(self):
        """학생 정보를 딕셔너리로 변환합니다."""

        return {
            "name": self.name,
            "scores": self.scores,
            "average": self.average(),
            "grade": self.grade(),
        }


def create_sample_students():
    """예제 학생 데이터를 생성합니다."""

    student_1 = Student("김민수")
    student_1.add_score(90)
    student_1.add_score(85)
    student_1.add_score(95)

    student_2 = Student("이서연")
    student_2.add_score(100)
    student_2.add_score(95)
    student_2.add_score(98)

    student_3 = Student("박지훈")
    student_3.add_score(70)
    student_3.add_score(75)
    student_3.add_score(80)

    return [student_1, student_2, student_3]


def print_students(students):
    """전체 학생의 성적 정보를 출력합니다."""

    print("[학생 성적 현황]")

    for student in students:
        information = student.to_dictionary()

        print(
            f"{information['name']}: "
            f"점수={information['scores']}, "
            f"평균={information['average']:.1f}, "
            f"등급={information['grade']}"
        )


def save_report(students, file_path):
    """전체 학생의 성적 보고서를 텍스트 파일로 저장합니다."""

    with file_path.open("w", encoding="utf-8") as file:
        file.write("[학생 성적 보고서]\n")

        for student in students:
            file.write(
                f"{student.name},"
                f"{student.average():.1f},"
                f"{student.grade()}\n"
            )


def main():
    """프로그램의 전체 실행 흐름을 관리합니다."""

    try:
        students = create_sample_students()

        print_students(students)

        # 평균 점수가 80점 이상인 학생만 추출합니다.
        passed_students = [
            student.name
            for student in students
            if student.average() >= 80
        ]

        print("평균 80점 이상:", passed_students)

        # 전체 학생의 등급을 집합으로 구성합니다.
        grade_set = {student.grade() for student in students}
        print("발생한 등급:", grade_set)

        # 학생 이름을 키로 사용하는 딕셔너리를 생성합니다.
        student_dictionary = {
            student.name: student.average()
            for student in students
        }

        print("학생별 평균:", student_dictionary)

        report_path = Path("student_report.txt")
        save_report(students, report_path)

        print("보고서 저장 완료:", report_path)

    except OSError as error:
        print("파일 처리 오류가 발생했습니다:", error)

    except ValueError as error:
        print("데이터 검증 오류가 발생했습니다:", error)

    finally:
        print("성적 관리 프로그램을 종료합니다.")


# 현재 파일을 직접 실행할 때만 main() 함수를 호출합니다.
if __name__ == "__main__":
    main()