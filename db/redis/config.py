import aioredis

redis: aioredis.Redis = aioredis.Redis.from_url(
    url='redis://localhost'
)
