"""제네릭을 이용하여 타입 안전한 스택을 구현합니다."""

from typing import Generic, TypeVar


# T는 스택이 저장할 요소 타입을 나타냅니다.
T = TypeVar("T")


class Stack(Generic[T]):
    """동일한 타입의 요소를 후입선출 방식으로 관리합니다."""

    def __init__(self) -> None:
        """빈 요소 리스트를 생성합니다."""

        self._items: list[T] = []

    def push(self, item: T) -> None:
        """스택의 끝에 요소를 추가합니다."""

        self._items.append(item)

    def pop(self) -> T:
        """마지막 요소를 제거하여 반환합니다."""

        if not self._items:
            raise IndexError("빈 스택입니다.")

        return self._items.pop()

    def __len__(self) -> int:
        """저장된 요소 개수를 반환합니다."""

        return len(self._items)


number_stack: Stack[int] = Stack()
number_stack.push(10)
number_stack.push(20)

text_stack: Stack[str] = Stack()
text_stack.push("Python")
text_stack.push("Data")

print("정수:", number_stack.pop())
print("문자열:", text_stack.pop())
print("남은 정수 개수:", len(number_stack))