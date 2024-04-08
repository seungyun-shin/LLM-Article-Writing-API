# Dockerfile
FROM python:3.8

WORKDIR /workspace

# COPY . /workspace

RUN pip install fastapi uvicorn python-dotenv openai langchain

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]