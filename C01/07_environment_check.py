"""현재 Python 실행 환경을 진단합니다."""

import os
import platform
import sys
from pathlib import Path


# 현재 Python의 상세 버전 정보입니다.
print("Python 버전:", sys.version.split()[0])

# 현재 코드를 실행하는 인터프리터 경로입니다.
print("인터프리터 경로:", sys.executable)

# 현재 운영체제 이름입니다.
print("운영체제:", platform.system())

# 현재 작업 디렉터리입니다.
print("작업 디렉터리:", Path.cwd())

# sys.prefix와 sys.base_prefix가 다르면 일반적으로 가상환경입니다.
is_virtual_environment = sys.prefix != sys.base_prefix
print("가상환경 활성화 여부:", is_virtual_environment)

# venv 활성화 시 설정되는 환경변수입니다.
print("가상환경 경로:", os.environ.get("VIRTUAL_ENV", "정보 없음"))