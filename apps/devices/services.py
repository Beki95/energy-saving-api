import uuid
from random import choice, choices

from sqlalchemy.engine import CursorResult

from db.postgres.type import DeviceType


async def generate_hex() -> str:
    return uuid.uuid4().hex


async def get_48_bit_mac() -> str:
    mac = [await generate_hex() for _ in range(3)]
    return ''.join(mac)


async def get_random_type() -> str:
    dev_type = choice(DeviceType.choice())
    return dev_type


async def get_random_data(ids: CursorResult, count: int):
    ids = [i[0] for i in ids]
    data = choices(ids, k=count)
    return data
