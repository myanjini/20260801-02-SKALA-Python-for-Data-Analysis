"""Optional 값을 안전하게 처리합니다."""


def find_user_name(user_id: int) -> str | None:
    """사용자 ID에 해당하는 이름을 반환하고 없으면 None을 반환합니다."""

    users: dict[int, str] = {
        1: "Alice",
        2: "Bob",
    }

    return users.get(user_id)


def create_greeting(name: str | None) -> str:
    """이름이 있으면 인사말을 만들고 없으면 기본 문구를 반환합니다."""

    if name is None:
        return "사용자를 찾을 수 없습니다."

    # None 검사를 통과한 뒤에는 name을 str로 안전하게 사용합니다.
    return f"안녕하세요,{name.upper()}님!"


print(create_greeting(find_user_name(1)))
print(create_greeting(find_user_name(99)))