"""구매 금액과 가입 기간에 따라 회원 등급을 판정합니다."""


# 회원의 누적 구매 금액입니다.
purchase_amount = 1_200_000

# 회원의 가입 기간입니다.
membership_years = 3

# 두 조건을 모두 만족하면 VIP 등급으로 판정합니다.
if purchase_amount >= 1_000_000 and membership_years >= 2:
    grade = "VIP"

# 구매 금액이 500,000원 이상이면 우수 등급으로 판정합니다.
elif purchase_amount >= 500_000:
    grade = "우수"

# 위 조건을 모두 만족하지 않으면 일반 등급으로 판정합니다.
else:
    grade = "일반"

print("회원 등급:", grade)

# 조건 표현식으로 배송비를 결정합니다.
shipping_fee = 0 if purchase_amount >= 50_000 else 3_000
print("배송비:", shipping_fee)