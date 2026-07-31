# 컴프리헨션 및 반복 제어 실습

names = ["Alice", "Bob", "Charlie", "David"]
salaries = [85000, 60000, 95000, 70000]

# 1. zip()을 활용한 딕셔너리 생성
emp_salary_map = {name: salary for name, salary in zip(names, salaries)}
print(f"직원 급여 맵: {emp_salary_map}")

# 2. 리스트 컴프리헨션과 조건문 필터링 (급여 70000 이상)
high_earners = [name for name, salary in emp_salary_map.items() if salary >= 70000]
print(f"고액 연봉자: {high_earners}")

# 3. 딕셔너리 값 가공 (급여 10% 인상 처리)
updated_salaries = {name: int(salary * 1.1) for name, salary in emp_salary_map.items()}
print(f"인상된 급여: {updated_salaries}")