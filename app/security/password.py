

class PasswordEncoder:

    def __call__(self, password):
        pass


class PasswordValidator:

    def __call__(self, plain_password: str, hashed_password: str) -> bool:
        pass
