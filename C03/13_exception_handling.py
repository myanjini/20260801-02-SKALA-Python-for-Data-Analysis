"""JSON 파일을 읽고 예외 유형별로 처리합니다."""

import json
from pathlib import Path


def load_config(file_path):
    """JSON 설정 파일을 읽고 필수 키를 확인합니다."""

    try:
        with file_path.open("r", encoding="utf-8") as file:
            config = json.load(file)

        # 대괄호 접근은 키가 없으면 KeyError를 발생시킵니다.
        input_path = config["input_path"]

    except FileNotFoundError:
        print("설정 파일을 찾을 수 없습니다.")
        return None

    except json.JSONDecodeError as error:
        print(f"JSON 형식 오류:{error.msg}")
        return None

    except KeyError as error:
        print(f"필수 설정 누락:{error}")
        return None

    else:
        print("설정 파일을 정상적으로 읽었습니다.")
        return input_path

    finally:
        print("설정 파일 읽기 작업을 종료합니다.")


config_path = Path("config.json")
result = load_config(config_path)
print("입력 경로:", result)