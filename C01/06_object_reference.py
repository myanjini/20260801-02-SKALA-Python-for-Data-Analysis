"""객체 참조와 리스트 복사의 차이를 확인합니다."""


# 원본 리스트 객체입니다.
original_scores = [80, 90]

# 같은 리스트 객체를 참조합니다.
shared_scores = original_scores

# 새로운 리스트 객체를 생성합니다.
copied_scores = original_scores.copy()

# is는 두 변수가 같은 객체를 참조하는지 확인합니다.
print("원본과 공유 객체 동일성:", original_scores is shared_scores)
print("원본과 복사본 동일성:", original_scores is copied_scores)

# 공유 객체를 통해 리스트를 수정합니다.
shared_scores.append(100)

print("원본:", original_scores)
print("공유 객체:", shared_scores)
print("복사본:", copied_scores)