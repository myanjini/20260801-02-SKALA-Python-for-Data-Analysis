"""분석 설정을 JSON 파일로 저장하고 다시 읽습니다."""

import json
from pathlib import Path


config_path = Path("analysis_config.json")

config = {
    "project": "매출 분석",
    "input": {
        "path": "data/sales.csv",
        "encoding": "utf-8",
    },
    "minimum_amount": 1000,
    "regions": ["서울", "부산", "대전"],
}

with config_path.open("w", encoding="utf-8") as file:
    # ensure_ascii=False는 한글을 유니코드 이스케이프로 바꾸지 않습니다.
    json.dump(config, file, ensure_ascii=False, indent=2)


with config_path.open("r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print("프로젝트:", loaded_config["project"])
print("입력 경로:", loaded_config["input"]["path"])
print("기준 금액:", loaded_config.get("minimum_amount", 0))
print("지역:", loaded_config["regions"])