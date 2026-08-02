"""함수를 이용하여 매출 요약 정보를 계산합니다."""


def summarize_sales(sales):
    """매출 리스트의 건수, 합계와 평균을 반환합니다."""

    # 함수 내부에서 생성한 지역 변수입니다.
    count = len(sales)

    # 빈 리스트일 때 0으로 나누는 오류를 방지합니다.
    if count == 0:
        return {
            "count": 0,
            "total": 0,
            "average": 0.0,
        }

    total = sum(sales)
    average = total / count

    # 여러 결과를 딕셔너리 하나로 반환합니다.
    return {
        "count": count,
        "total": total,
        "average": average,
    }


daily_sales = [120000, 150000, 90000]
summary = summarize_sales(daily_sales)

print("거래 건수:", summary["count"])
print("총매출:", summary["total"])
print(f"평균 매출:{summary['average']:.1f}")