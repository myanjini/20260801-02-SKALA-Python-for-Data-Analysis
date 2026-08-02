"""tmp_path를 이용하여 JSON 파일 처리를 검증합니다."""

import json
from pathlib import Path


def save_json(data: list[dict[str, object]], file_path: Path) -> None:
    """데이터를 JSON 파일로 저장합니다."""

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def load_json(file_path: Path) -> list[dict[str, object]]:
    """JSON 파일을 읽어 반환합니다."""

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def test_json_round_trip(tmp_path: Path) -> None:
    """저장 후 다시 읽은 데이터가 원본과 같은지 검증합니다."""

    file_path = tmp_path / "result.json"
    original = [{"region": "서울", "amount": 1500}]

    save_json(original, file_path)
    loaded = load_json(file_path)

    assert file_path.exists()
    assert loaded == original