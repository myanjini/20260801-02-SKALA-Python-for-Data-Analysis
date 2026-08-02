# 단락 평가 및 조건부 표현식 활용 실습

# 1. 단락 평가를 통한 객체 참조 안전성 확보
user = None
# user가 None이므로 user.is_active는 평가되지 않아 AttributeError가 발생하지 않습니다.
if user and user.is_active:
    print("활성화된 사용자입니다.")
else:
    print("사용자 정보가 없거나 비활성화 상태입니다.")

# 2. 삼항 연산자 (조건부 표현식)
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"시험 결과: {result}")

# 3. in 및 not in 키워드 활용
allowed_roles = ["admin", "manager"]
user_role = "user"

if user_role not in allowed_roles:
    print("접근 권한이 없습니다.")