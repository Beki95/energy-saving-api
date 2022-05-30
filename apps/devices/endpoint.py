from fastapi import APIRouter, Depends, Response
from starlette import status

from db.postgres.dependencies import get_session
from repositories.devices import DeviceRepository
from repositories.endpoints import EndpointRepository
from schemas.devices import ListDeviceScheme
from specifications.base_specific import BaseSpecific
from specifications.devices.device_specific import DeviceSpecific
from specifications.devices.endpoint_specific import EndpointSpecific

devices_router = APIRouter()


@devices_router.post('/')
async def create_devices(db=Depends(get_session),
                         device_spec: BaseSpecific = Depends(DeviceSpecific),
                         endpoint_spec: BaseSpecific = Depends(EndpointSpecific)):
    result = await DeviceRepository(db).create(await device_spec())
    await EndpointRepository(db).create(await endpoint_spec(result))
    return Response(status_code=status.HTTP_201_CREATED)


@devices_router.get('/', response_model=list[ListDeviceScheme])
async def get_devices(db=Depends(get_session)):
    devices = await DeviceRepository(db).filter()
    return list(devices)
