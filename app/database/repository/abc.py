from app.database import LocalSession


class DAO:
    """
    By below code as using __call__,
    you can manage Session without __init__, __enter__, __exit__

    def __call__():
        with LocalSession() as session:
            self.session = session
            try:
                yield self
            except Exception as e:
                raise e
            finally:
                self.session.close()
    """

    def __init__(self):
        self.session = LocalSession()

    def __call__(self):
        with self as repository:
            yield repository

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
