from pydantic import BaseModel


class EndpointScheme(BaseModel):
    device_id: int
