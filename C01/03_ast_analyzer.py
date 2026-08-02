"""소스코드를 추상 구문 트리로 분석합니다."""

import ast  # 추상 구문 트리 생성과 탐색 기능을 제공합니다.


source_code = """
price = 10000
tax = price * 0.1
total = price + tax
print(total)
"""

# ast.parse()는 소스코드를 추상 구문 트리로 변환합니다.
tree = ast.parse(source_code)

print("[추상 구문 트리]")
print(ast.dump(tree, indent=2))

variable_names = []
called_functions = []

# ast.walk()는 트리의 모든 노드를 순회합니다.
for node in ast.walk(tree):
    # ast.Name은 변수명이나 함수명 등의 식별자를 나타냅니다.
    if isinstance(node, ast.Name):
        variable_names.append(node.id)

    # ast.Call은 함수 호출을 나타냅니다.
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        called_functions.append(node.func.id)

print("사용된 이름:", sorted(set(variable_names)))
print("호출된 함수:", sorted(set(called_functions)))