import os
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world "}


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
