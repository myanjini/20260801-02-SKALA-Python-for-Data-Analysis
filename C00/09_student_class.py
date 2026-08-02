"""학생 정보를 표현하는 클래스를 정의하는 예제입니다."""


class Student:
    """학생의 이름과 점수를 관리하는 클래스입니다."""

    def __init__(self, name, scores=None):
        """Student 인스턴스의 초기값을 설정합니다."""

        # self.name은 학생의 이름을 저장하는 인스턴스 변수입니다.
        self.name = name

        # 전달된 점수가 없으면 빈 리스트를 새로 생성합니다.
        self.scores = scores if scores is not None else []

    def add_score(self, score):
        """점수를 학생의 점수 리스트에 추가합니다."""

        # 점수의 유효 범위를 확인합니다.
        if not 0 <= score <= 100:
            raise ValueError("점수는 0부터 100 사이여야 합니다.")

        self.scores.append(score)

    def calculate_average(self):
        """학생의 평균 점수를 계산하여 반환합니다."""

        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)

    def print_summary(self):
        """학생 이름, 점수, 평균을 화면에 출력합니다."""

        average = self.calculate_average()

        print(f"학생: {self.name}")
        print(f"점수: {self.scores}")
        print(f"평균: {average:.1f}")


# Student 클래스를 바탕으로 첫 번째 인스턴스를 생성합니다.
student_1 = Student("김민수", [80, 90])

# 메서드를 호출하여 점수를 추가합니다.
student_1.add_score(100)

# 학생 정보를 출력합니다.
student_1.print_summary()


# 같은 클래스로 별도의 인스턴스를 생성합니다.
student_2 = Student("이서연")
student_2.add_score(95)
student_2.print_summary()