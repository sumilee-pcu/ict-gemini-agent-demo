# ICT Mini AI Agent

Python FastAPI와 Gemini API로 구현하는 미니 AI 에이전트.
ICT폴리텍대학 교육중점교원 시범강의 및 학생 실습용 예제입니다.

생성형 AI를 웹시스템 안에서 안전하게 호출하는 서버 측 구조를 다룹니다.
핵심 흐름: 요청 → 검증 → 프롬프트 → 모델 호출 → 응답 반환

## 1. 코랩으로 바로 실습 (설치 불필요)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sumilee-pcu/ict-gemini-agent-demo/blob/main/ICT_Mini_AI_Agent_Colab.ipynb)

위 배지를 누르면 브라우저에서 바로 실행됩니다. 노트북 셀을 위에서부터 차례로 실행하세요.

API 키는 코랩 왼쪽 열쇠(보안 비밀) 아이콘에서 이름 `GEMINI_API_KEY`로 등록합니다.
키 발급: https://aistudio.google.com/apikey

## 2. 로컬 실행 (FastAPI 서버)

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="발급받은_API_키"     # Windows: $env:GEMINI_API_KEY="..."
uvicorn app:app --reload
```

요청 테스트:

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"AI 에이전트와 일반 챗봇의 차이는 무엇인가요?"}'
```

API 키 없이 서버 구조만 확인하려면 `MOCK_MODE=true`로 실행합니다.

## 3. 사용 모델

기본 모델은 `gemini-3-flash`입니다. 환경변수 `GEMINI_MODEL`로 바꿀 수 있습니다.
안정 모델명은 https://ai.google.dev/gemini-api/docs/models 에서 확인하세요.

## 4. 보안 원칙

- `GEMINI_API_KEY`는 코드, 노트북, 깃 저장소에 저장하지 않습니다.
- 브라우저나 클라이언트에서 Gemini API를 직접 호출하지 않고 서버를 거칩니다.
- 시연에서는 호출을 최소화하고 질문 길이를 제한합니다.

## 파일

| 파일 | 설명 |
|---|---|
| `ICT_Mini_AI_Agent_Colab.ipynb` | 코랩 실습 노트북 (직접 호출 + FastAPI 체험 + 과제) |
| `app.py` | FastAPI 서버 (로컬 실행용) |
| `requirements.txt` | 패키지 목록 |
