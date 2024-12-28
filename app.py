from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World. This is the first commit"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)