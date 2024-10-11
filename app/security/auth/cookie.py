from typing import Callable
from fastapi import Cookie as Cookie_

from .abc import Authorization


class Cookie(Authorization):

    def __call__(self, token: Callable = Cookie_(alias='Authorization')):
        pass

    def refresh_token(self, token: Callable = Cookie_(alias='REFRESH_TOKEN')):
        pass
