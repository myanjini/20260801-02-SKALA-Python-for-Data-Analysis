"""중첩 Pydantic 모델로 분석 결과를 구성합니다."""

from pydantic import BaseModel, Field, computed_field


class SalesItem(BaseModel):
    """개별 매출 항목을 표현합니다."""

    region: str = Field(min_length=1)
    amount: float = Field(gt=0)


class AnalysisResult(BaseModel):
    """여러 매출 항목과 분석명을 포함합니다."""

    analysis_name: str
    items: list[SalesItem]

    @computed_field
    @property
    def total_amount(self) -> float:
        """전체 매출 합계를 계산합니다."""

        return sum(item.amount for item in self.items)


result = AnalysisResult.model_validate(
    {
        "analysis_name": "지역 매출",
        "items": [
            {"region": "서울", "amount": 1500},
            {"region": "부산", "amount": 2200},
        ],
    }
)

print("분석명:", result.analysis_name)
print("첫 지역:", result.items[0].region)
print("총매출:", result.total_amount)
print("직렬화:", result.model_dump())