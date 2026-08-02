"""소스 파일을 바이트코드로 컴파일합니다."""

import py_compile  # Python 소스 파일을 바이트코드로 컴파일합니다.
from pathlib import Path


# 컴파일 대상 파일을 생성하지 않고 현재 파일 자체를 대상으로 사용합니다.
source_path = Path(__file__)

# py_compile.compile()은 .py 파일을 .pyc 파일로 컴파일합니다.
compiled_path = py_compile.compile(
    str(source_path),
    doraise=True,
)

print("소스 파일:", source_path.name)
print("컴파일 성공:", Path(compiled_path).exists())
print("캐시 디렉터리:", Path(compiled_path).parent.name)
print("캐시 파일:", Path(compiled_path).name)