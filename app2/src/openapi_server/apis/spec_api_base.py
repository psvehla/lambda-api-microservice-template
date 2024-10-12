# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401



class BaseSpecApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSpecApi.subclasses = BaseSpecApi.subclasses + (cls,)
    async def get_open_api_spec_yaml(
        self,
    ) -> str:
        ...
