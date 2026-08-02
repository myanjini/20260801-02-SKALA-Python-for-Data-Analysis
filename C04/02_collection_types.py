"""컬렉션과 중첩 자료구조에 타입 힌트를 적용합니다."""


def calculate_subject_averages(
    records: list[dict[str, int | str]],
) -> dict[str, float]:
    """학생 레코드에서 과목별 평균을 계산합니다."""

    subject_totals: dict[str, int] = {}
    subject_counts: dict[str, int] = {}

    for record in records:
        subject = str(record["subject"])
        score = int(record["score"])

        subject_totals[subject] = subject_totals.get(subject, 0) + score
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {
        subject: total / subject_counts[subject]
        for subject, total in subject_totals.items()
    }


score_records: list[dict[str, int | str]] = [
    {"student": "철수", "subject": "수학", "score": 90},
    {"student": "영희", "subject": "수학", "score": 80},
    {"student": "민수", "subject": "영어", "score": 95},
]

averages: dict[str, float] = calculate_subject_averages(score_records)
print(averages)