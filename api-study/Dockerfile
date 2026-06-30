# 1. Python 공식 경량화 이미지 사용
FROM python:3.12-slim

# 2. 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY . .

# 5. Uvicorn 서버 실행 (FastAPI 기본 WAS)
CMD ["uvicorn", "core.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]