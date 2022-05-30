import aioredis

from core.config import settings

redis: aioredis.Redis = aioredis.Redis.from_url(
    url=settings.REDIS_URL
)
