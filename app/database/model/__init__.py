from app.database.abc import Base


def create_all(engine):
    from app.database.model.user import User

    Base.metadata.create_all(bind=engine)
