from apps.devices.services import get_random_type, get_48_bit_mac
from schemas.devices import DeviceScheme
from specifications.base_specific import BaseSpecific


class DeviceSpecific(BaseSpecific):

    def __init__(self, default: int = 10):
        self.default = default

    async def __call__(self, *args, **kwargs):
        devices = [DeviceScheme(dev_type=await get_random_type(),
                                dev_id=await get_48_bit_mac()).dict()
                   for _ in range(self.default)]
        return devices
