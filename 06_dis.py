import dis

def add(x, y):
    return x + y

dis.dis(add)
# 출력 결과 예시:
# LOAD_FAST (x를 스택에 올림)
# LOAD_FAST (y를 스택에 올림)
# BINARY_OP (+) (두 값을 더함)
# RETURN_VALUE (결과 반환)