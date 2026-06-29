# from fastapi import FastAPI
# import uvicorn

# app = FastAPI(title="Study")

# @app.get('/')
# def read_root():
#     return {"Hello": "World"}

# @app.get('/add')
# def add_numbers(a: int, b: int):
#     return {"result": str(a + b)}

# # =======
# # 숙제: 각자 api 하나씩 만들고 테스트하기
# # - 무엇이든, 만들고 싶은 기능을 API화해서 요청에 대해 서버가 처리하도 되돌려주도록 만들기.
# # - 간단한 기능이여도 OK (단순 계산, 문자열 붙이기 등등)
# # - 기능에 맞는 URL 이름 지정
# # - get 방식으로, URL 파라미터를 받아 처리
# # =======

# # 숙제 - 우재성 : 생년월일로 나이 계산 API
# @app.get('/get_age')
# def get_age(birth_date: str):
#     # 연도로 나이 계산
#     from datetime import datetime
#     bd = datetime.strptime(birth_date, "%Y%m%d")
#     today = datetime.now()
#     age = today.year - bd.year
#     # 생일이 안지났으면 나이에서 1 빼기
#     if (today.month, today.day) < (bd.month, bd.day):
#         age -= 1

#     return {
#         "current_age": str(age)
#     }


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
import uvicorn

# 1. 서버 생성 (반드시 가장 위!)
app = FastAPI()

# 2. BMI API 등록 (반드시 uvicorn.run 보다 위!)
@app.get("/bmi")
def calculate_bmi(height: float, weight: float):
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)
    
    if bmi < 18.5:
        status = "저체중"
    elif bmi < 23:
        status = "정상"
    elif bmi < 25:
        status = "과체중"
    else:
        status = "비만"
        
    return {
        "message": "BMI 계산 성공!",
        "bmi": bmi,
        "status": status
    }

# 3. 서버 실행 (반드시 파일의 가장 맨 마지막 줄!)
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)