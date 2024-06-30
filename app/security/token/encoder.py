from datetime import datetime, timedelta
from typing import Tuple

from jwt import encode

from app.config import JWTConfig
from app.security.token.data import Payload


class Encoder:

    def __call__(self, user_id: int, key: str, exp: float) -> Tuple[str, float]:
        payload = Payload(
            exp=exp,
            sub=user_id
        )
        token = encode(
            key=key,
            payload=payload.dict()
        )
        return token, exp

    def access_token(self, user_id: int) -> Tuple[str, float]:
        utc = datetime.utcnow()
        term = timedelta(seconds=JWTConfig.ACCESS_EXP)

        exp = (utc + term).timestamp()

        return self(user_id, key="", exp=exp)

    def refresh_token(self, user_id: int) -> Tuple[str, float]:
        utc = datetime.utcnow()
        term = timedelta(seconds=JWTConfig.REFRESH_EXP)

        exp = (utc + term).timestamp()

        return self(user_id, key="", exp=exp)
