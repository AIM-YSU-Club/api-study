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

# 숙제 - 조범준 : BMI 계산기 API
@app.get('/BMI')
def Calculte_BMI(Weight_kg: float, height_cm: float):
    # 키를 미터(m)단위로 변환
    height_m = height_cm / 100
    # BMI = 체중(kg) / 키(m) * 키 (m)
    bmi = Weight_kg / (height_m ** 2)

    return {
        "weight" : Weight_kg,
        "height" : height_cm,
        "bmiscore" : str(round(bmi, 2)) # 소수점 둘째짜리까지 반올림 
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)