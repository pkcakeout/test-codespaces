from fastapi import FastAPI
from app.api.v1.test_endpoints import router as test_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI assisted FastAPI application!"}

app.include_router(test_router)
