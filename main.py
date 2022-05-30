import uvicorn
from fastapi import FastAPI

from apps.anagram import anagram_router
from apps.devices.endpoint import devices_router
from db.postgres.config import Base, engine
from db.redis.config import redis

app = FastAPI()

app.include_router(anagram_router, prefix='/checking_anagram', tags=['anagram'])
app.include_router(devices_router, prefix='/device', tags=['device'])


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event('shutdown')
async def shutdown():
    await redis.close()


if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8000, host="0.0.0.0", reload=True)
