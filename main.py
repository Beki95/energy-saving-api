from fastapi import FastAPI
import uvicorn

from apps.anagram import anagram_router

app = FastAPI()

app.include_router(anagram_router, prefix='/checking_anagram', tags=['anagram'])

if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8000, host="0.0.0.0", reload=True)
