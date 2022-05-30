from apps.devices.services import get_random_data
from schemas.endpoints import EndpointScheme
from specifications.base_specific import BaseSpecific
from sqlalchemy.engine.cursor import CursorResult


class EndpointSpecific(BaseSpecific):

    def __init__(self):
        self.default = 5

    async def __call__(self, devices_ids: CursorResult):
        devices_ids = await get_random_data(devices_ids, self.default)
        ids = [EndpointScheme(device_id=i).dict() for i in devices_ids]
        return ids
