from sqlalchemy import insert

from db.postgres.entity.endpoints import Endpoint
from repositories.base import BaseRepository


class EndpointRepository(BaseRepository):

    async def create(self, devices_ids: list[dict, ...]):
        query = (
            insert(Endpoint).values(devices_ids)
        )
        result = await self.db.execute(query)
        return result
