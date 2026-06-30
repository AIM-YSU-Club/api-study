from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Study")


@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/add')
def add_numbers(a: int, b: int):
    return {"result": str(a + b)}

# =======
# 숙제: 각자 api 하나씩 만들고 테스트하기
# - 무엇이든, 만들고 싶은 기능을 API화해서 요청에 대해 서버가 처리하도 되돌려주도록 만들기.
# - 간단한 기능이여도 OK (단순 계산, 문자열 붙이기 등등)
# - 기능에 맞는 URL 이름 지정
# - get 방식으로, URL 파라미터를 받아 처리
# =======

# 숙제 - 우재성 : 생년월일로 나이 계산 API


@app.get('/get_age')
def get_age(birth_date: str):
    # 연도로 나이 계산
    from datetime import datetime
    bd = datetime.strptime(birth_date, "%Y%m%d")
    today = datetime.now()
    age = today.year - bd.year
    # 생일이 안지났으면 나이에서 1 빼기
    if (today.month, today.day) < (bd.month, bd.day):
        age -= 1

    return {
        "current_age": str(age)
    }


# 숙제 - 홍서준 : 원화를 달러로 환전해주는 API
exchange_usd = 1550  # 2026.06.30 기준 환율


@app.get('/get_exchange')  # url 파라미터 생성
def get_exchange(krw: float):  # krw 타입 명시

    # 환전
    usd = krw / exchange_usd

    # json 형식으로 출력
    return {
        "원화": krw,
        "환율": exchange_usd,
        "환전된 금액(달러)": round(usd, 2)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
