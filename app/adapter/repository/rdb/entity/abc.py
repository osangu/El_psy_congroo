from typing import Tuple

from sqlalchemy import Column, Table
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Entity:
    table_name: str
    fields: Tuple[Column]

    _base = Base
    __table = None

    @classmethod
    @property
    def table(cls) -> Table:
        if cls.__table is None:
            cls.__table = Table(
                cls.table_name,
                cls._base.metadata,
                *cls.fields
            )

        return cls.__table

    @classmethod
    def mapper(cls, model: object, properties: dict):
        cls._base._sa_registry.map_imperatively(
            class_=model,
            local_table=cls.table,
            properties=properties
        )
