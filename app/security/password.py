from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


class PasswordEncoder:

    def __call__(self, password):
        return pwd_context.hash(password)


class PasswordVerifier:

    def __call__(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
