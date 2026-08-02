"""클로저로 설정값을 기억하는 함수를 생성합니다."""


def create_tax_calculator(tax_rate):
    """지정된 세율을 기억하는 계산 함수를 반환합니다."""

    def calculate(amount):
        """외부 함수의 tax_rate를 사용하여 세금을 계산합니다."""

        return amount * tax_rate

    return calculate


# 서로 다른 세율을 기억하는 두 함수를 생성합니다.
vat_calculator = create_tax_calculator(0.1)
reduced_calculator = create_tax_calculator(0.05)

print("10% 세금:", vat_calculator(100000))
print("5% 세금:", reduced_calculator(100000))

# __closure__를 통해 외부 변수 보관 여부를 확인할 수 있습니다.
print("기억한 값:", vat_calculator.__closure__[0].cell_contents)