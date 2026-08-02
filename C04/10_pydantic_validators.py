"""Pydantic 필드 검증기와 모델 검증기를 사용합니다."""

from typing import Self

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


class AnalysisRequest(BaseModel):
    """기간별 지역 분석 요청을 표현합니다."""

    region: str = Field(min_length=1)
    start_month: int = Field(ge=1, le=12)
    end_month: int = Field(ge=1, le=12)

    @field_validator("region")
    @classmethod
    def normalize_region(cls, value: str) -> str:
        """지역명의 양쪽 공백을 제거하고 빈 값을 차단합니다."""

        clean_value = value.strip()

        if not clean_value:
            raise ValueError("지역은 비어 있을 수 없습니다.")

        return clean_value

    @model_validator(mode="after")
    def validate_period(self) -> Self:
        """종료 월이 시작 월보다 빠르지 않은지 확인합니다."""

        if self.end_month < self.start_month:
            raise ValueError("종료 월은 시작 월보다 빠를 수 없습니다.")

        return self


try:
    request = AnalysisRequest(
        region=" 서울 ",
        start_month=3,
        end_month=8,
    )
except ValidationError as error:
    print(error)
else:
    print(request.model_dump())