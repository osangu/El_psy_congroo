from .abc import Authorization

from .cookie import Cookie as CookieAuthorization
from .header import Header as HeaderAuthorization


class Auth:
    cookie: Authorization = CookieAuthorization
    header: Authorization = HeaderAuthorization
