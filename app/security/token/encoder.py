from jwt import encode

from app.security.token.data import Payload


class Encoder:

    def __call__(self, user_id: int, key: str, exp: float) -> str:
        payload = Payload(
            exp=exp,
            sub=user_id
        )
        return encode(
            key=key,
            payload=payload.dict()
        )

    def access_token(self, user_id: int) -> str:
        return self(user_id, key="", exp=float())  # TODO

    def refresh_token(self, user_id: int) -> str:
        return self(user_id, key="", exp=float())
