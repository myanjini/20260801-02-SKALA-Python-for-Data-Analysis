"""기본 인자와 키워드 인자의 사용 방법을 확인합니다."""


def create_report(name, score, title="성적 보고서", *, precision=1):
    """학생 이름과 점수를 지정한 형식으로 반환합니다."""

    # precision은 * 뒤에 있으므로 키워드로만 전달합니다.
    return f"[{title}]{name}:{score:.{precision}f}점"


def add_tag(tag, tags=None):
    """호출마다 독립적인 태그 리스트를 생성합니다."""

    # 가변 기본값 공유를 피하기 위한 안전한 초기화입니다.
    if tags is None:
        tags = []

    tags.append(tag)
    return tags


print(create_report("김민수", 87.456))
print(create_report("이서연", 95.678, title="중간고사", precision=2))

print(add_tag("Python"))
print(add_tag("Data"))