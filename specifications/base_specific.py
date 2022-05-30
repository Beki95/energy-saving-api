from abc import ABC, abstractmethod


class BaseSpecific(ABC):

    @abstractmethod
    def __init__(self, default: int):
        self.default = default

    @abstractmethod
    async def __call__(self, *args, **kwargs): ...
