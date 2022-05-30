from sqlalchemy import insert, select, func

from db.postgres.entity.devices import Device
from db.postgres.entity.endpoints import Endpoint
from db.postgres.type import DeviceType
from repositories.base import BaseRepository


class DeviceRepository(BaseRepository):

    async def create(self, devices: list[dict, ...]):
        query = (
            insert(Device).values(devices).returning(Device.id)
        )
        result = await self.db.execute(query)
        return result

    async def filter(self):
        query = (
            select(
                Device.id, Device.dev_type, Device.dev_id,
                select(
                    func.count(Device.id)
                ).where(Device.dev_type == DeviceType.LORA).label(DeviceType.LORA),
                select(
                    func.count(Device.id)
                ).where(Device.dev_type == DeviceType.GSM).label(DeviceType.GSM),
                select(
                    func.count(Device.id)
                ).where(Device.dev_type == DeviceType.ZIGBEE).label(DeviceType.ZIGBEE),
                select(
                    func.count(Device.id)
                ).where(Device.dev_type == DeviceType.EMETER).label(DeviceType.EMETER)
            ).join(Endpoint, Device.id == Endpoint.device_id, isouter=True).where(
                Endpoint.id == None
            ).group_by(Device.id)
        )
        result = await self.db.execute(query)
        return result
