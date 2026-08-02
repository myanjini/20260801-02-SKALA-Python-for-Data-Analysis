"""환경변수에서 애플리케이션 설정을 읽습니다."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """실행에 필요한 환경 설정을 표현합니다."""

    api_key: str
    debug: bool
    db_host: str
    db_port: int


def require_environment(name):
    """필수 환경변수를 읽고 누락 시 오류를 발생시킵니다."""

    value = os.getenv(name)

    if value is None or not value.strip():
        raise RuntimeError(f"필수 환경변수 누락:{name}")

    return value


def load_settings():
    """환경변수를 읽어 Settings 객체를 생성합니다."""

    # 현재 디렉터리의 .env 파일을 불러옵니다.
    load_dotenv()

    return Settings(
        api_key=require_environment("API_KEY"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
        db_host=os.getenv("DB_HOST", "localhost"),
        db_port=int(os.getenv("DB_PORT", "5432")),
    )


settings = load_settings()

# API 키의 실제 값은 출력하지 않습니다.
print("API 키 설정 여부:", bool(settings.api_key))
print("디버그 모드:", settings.debug)
print("DB 호스트:", settings.db_host)
print("DB 포트:", settings.db_port)