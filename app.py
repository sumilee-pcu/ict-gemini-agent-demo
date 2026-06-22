import os

from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel, Field


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3-flash")
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"

app = FastAPI(title="ICT Mini AI Agent")


class AskRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=300)


class AskResponse(BaseModel):
    answer: str
    model: str


def build_prompt(question: str) -> str:
    return f"""
너는 ICT폴리텍 학생을 돕는 AI 학습 도우미다.
아래 질문에 대해 초급 학습자도 이해할 수 있게 5문장 이내로 답하라.
가능하면 실무 예시를 1개 포함하라.

질문: {question}
""".strip()


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    if MOCK_MODE:
        return AskResponse(
            answer=f"실습 모드 응답입니다. 질문 '{request.question}'에 대해 서버가 정상 동작했습니다.",
            model="mock",
        )

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY 환경변수가 설정되어 있지 않습니다.",
        )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=build_prompt(request.question),
    )

    return AskResponse(answer=response.text, model=MODEL_NAME)
