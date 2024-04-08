import os
from fastapi import FastAPI, HTTPException
from models import TextGenerationRequest,TextGenerationResponse
import uvicorn
from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks import get_openai_callback
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from templates import article_writing_template, token_check_template


# API KEY 정보로드
load_dotenv()

# 모델 로드 및 초기화
# client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# 객체 생성
model = ChatOpenAI(
    temperature=1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=4096,  # 최대 토큰수
    model_name="gpt-4-0125-preview",  # 모델명
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

output_parser = StrOutputParser()

app = FastAPI(
    title="article writing LLM model API",
    version="1.0",
    description = ""
)

@app.get("/")
def read_root():
    return {"article generate model API running..."}

@app.post("/token-check")
async def generate_text():

    with get_openai_callback() as cb:
    
        result = model.invoke(token_check_template)
        print(cb)

    return 'End'

@app.post("/generate-text", response_model=TextGenerationResponse)
async def generate_text(request: TextGenerationRequest):


    # 요청된 정보를 기반으로 프롬프트 구성
    prompt = PromptTemplate.from_template(article_writing_template)
    # 체인 구성
    chain = prompt | model | output_parser
    # 응답 생성
    response = chain.invoke({"category": request.category , "article_format": request.article_format ,"body_text": request.body_text, "highlight_text" : request.highlight_text})
    # print(chain.invoke({"body_text": request.body_text, "highlight_text" : request.highlight_text}))

    return TextGenerationResponse(status="success", generated_text=response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)