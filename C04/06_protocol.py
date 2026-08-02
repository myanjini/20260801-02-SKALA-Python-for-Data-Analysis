"""Protocol로 여러 저장기 구현의 공통 인터페이스를 정의합니다."""

from typing import Protocol


class RecordSaver(Protocol):
    """레코드 저장기가 제공해야 하는 메서드를 정의합니다."""

    def save(self, record: dict[str, object]) -> None:
        """레코드를 저장합니다."""

        ...


class MemorySaver:
    """레코드를 메모리 리스트에 저장합니다."""

    def __init__(self) -> None:
        self.records: list[dict[str, object]] = []

    def save(self, record: dict[str, object]) -> None:
        self.records.append(record)


class ConsoleSaver:
    """레코드를 콘솔에 출력합니다."""

    def save(self, record: dict[str, object]) -> None:
        print("콘솔 저장:", record)


def persist_record(saver: RecordSaver, record: dict[str, object]) -> None:
    """프로토콜을 만족하는 저장기에 레코드를 전달합니다."""

    saver.save(record)


record: dict[str, object] = {"region": "서울", "amount": 1500}

memory_saver = MemorySaver()
persist_record(memory_saver, record)
persist_record(ConsoleSaver(), record)

print("메모리 저장:", memory_saver.records)