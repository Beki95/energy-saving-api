from sqlalchemy import insert

from db.postgres.entity.devices import Device
from repositories.base import BaseRepository


class DeviceRepository(BaseRepository):

    async def create(self, devices: list[dict, ...]):
        query = (
            insert(Device).values(devices).returning(Device.id)
        )
        result = await self.db.execute(query)
        return result

    async def filter(self): ...
