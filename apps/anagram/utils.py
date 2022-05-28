from abc import ABC, abstractmethod

from apps.anagram.services import quick_sort
from db.redis.config import redis
from schemas.anagram import AnagramScheme, AnagramResponseScheme


class Check(ABC):

    @abstractmethod
    def __init__(self, scheme: AnagramScheme) -> None: ...

    @abstractmethod
    async def __call__(self, *args, **kwargs) -> AnagramResponseScheme: ...


class Checker(Check):

    def __init__(self, scheme: AnagramScheme):
        self.scheme = scheme

    async def __call__(self, *args, **kwargs) -> bool:
        status = False
        if await quick_sort(self.scheme.f_word) == \
                await quick_sort(self.scheme.s_word):
            status = True
        return status


class Count(ABC):

    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    async def __call__(self, *args, **kwargs) -> int: ...


class Counter(Count):

    def __init__(self):
        ...

    async def __call__(self, *args, **kwargs) -> int:
        status = kwargs.get('status', False)
        count = await redis.get('count')
        if status:
            count = int(count) + 1 if count else 0
            await redis.set(name='count', value=count)
        return count
