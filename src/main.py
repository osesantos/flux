from fastapi import FastAPI
from src.router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to Flux - LLM Orchestration Framework. Flux is up and running!"}
