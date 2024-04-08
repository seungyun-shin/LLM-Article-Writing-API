from pydantic import BaseModel, validator

# 요청 본문을 위한 모델 정의
class TextGenerationRequest(BaseModel):
    article_format: str
    category: str
    body_text: str
    highlight_text: str

    # article_format 필드에 대한 유효성 검사
    @validator('article_format')
    def check_article_format(cls, v):
        if v not in ["역피라미드형", "혼합형", "피라미드형"]:
            raise ValueError("기사의 형식입력값은 '역피라미드형', '혼합형', '피라미드형' 세개 중 하나여야 합니다.")
        return v

# 출력 값 정의
class TextGenerationResponse(BaseModel):
    status: str
    generated_text: str