from typing import Callable

from fastapi import Header as Header_

from .abc import Authorization


class Header(Authorization):

    def __call__(self, token: Callable = Header_('Authorization')):
        pass

    def refresh_token(self, token: Callable = Header_('REFRESH_TOKEN')):
        pass
