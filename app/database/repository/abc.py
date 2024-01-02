from app.database import LocalSession


class DAO:

    def __init__(self):
        self.session = LocalSession()

    def __call__(self):
        """
        Manage Session Without `__init__`, `__enter__`, `__exit__`

        with LocalSession() as session:
            self.session = session
            try:
                yield self
            except Exception as e:
                raise e
            finally:
                self.session.close()
        """
        with self as repository:
            yield repository

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
