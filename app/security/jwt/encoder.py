from typing import Union
from datetime import datetime, timedelta

from jwt import encode

from app.security.auth import Role
from app.security.jwt.payload import EXP, SUB, ROLE, TYPE
from app.util import kst_now
from app.config import JWTConfig


class Encoder:

    @staticmethod
    def __encode(
            user_id: int, role: Role,
            token_type: str, key: str, expired_sec: int
    ) -> Union[str, datetime]:
        expired_at = kst_now() + timedelta(seconds=expired_sec)
        token = encode(
            payload={
                EXP: expired_at.timestamp(),
                SUB: user_id,
                ROLE: role.value,
                TYPE: token_type
            },
            key=key,
            algorithm=JWTConfig.ALGORITHM
        )
        return token, expired_at

    @staticmethod
    def access_token(user_id: int, role: Role) -> Union[str, datetime]:
        key = JWTConfig.ACCESS_EXP_SEC
        token_type = JWTConfig.ACCESS
        expired_sec = int(JWTConfig.ACCESS_EXP_SEC)

        return Encoder.__encode(user_id, role, token_type, key, expired_sec)

    @staticmethod
    def refresh_token(user_id: int, role: Role) -> Union[str, datetime]:
        key = JWTConfig.REFRESH_EXP_SEC
        token_type = JWTConfig.REFRESH
        expired_sec = int(JWTConfig.REFRESH_EXP_SEC)

        return Encoder.__encode(user_id, role, token_type, key, expired_sec)
