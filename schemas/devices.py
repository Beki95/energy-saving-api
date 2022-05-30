from pydantic import BaseModel


class BaseDeviceScheme(BaseModel):
    dev_type: str
    dev_id: str


class DeviceScheme(BaseDeviceScheme):
    ...


class ListDeviceScheme(BaseDeviceScheme):
    id: int
    lora: int
    emeter: int
    zigbee: int
    gsm: int
