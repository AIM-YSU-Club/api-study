from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Study")

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/add')
def add_numbers(a: int, b: int):
    return {"result": str(a + b)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)