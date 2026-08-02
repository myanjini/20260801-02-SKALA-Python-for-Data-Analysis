"""여러 표준 라이브러리의 기본 기능을 사용합니다."""

import math
import re
from datetime import date, timedelta


# math.sqrt()는 제곱근을 반환합니다.
print("16의 제곱근:", math.sqrt(16))

# math.ceil()은 올림한 정수를 반환합니다.
print("3.2의 올림:", math.ceil(3.2))


start_date = date(2026, 8, 1)
end_date = start_date + timedelta(days=7)

print("시작일:", start_date)
print("7일 후:", end_date)


email = "user@example.com"
email_pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

# re.fullmatch()는 전체 문자열이 패턴과 일치하는지 확인합니다.
is_valid_email = re.fullmatch(email_pattern, email) is not None
print("이메일 형식:", is_valid_email)