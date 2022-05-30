from pydantic import BaseModel


class DeviceScheme(BaseModel):
    dev_type: str
    dev_id: str
