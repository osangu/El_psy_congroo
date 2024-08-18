from typing import Type


class Factory:
    _key_type = Type
    _abstract = Type
    _objects: dict

    def __new__(cls, key: _key_type, *args, **kwargs) -> _abstract:
        class_ = cls._objects.get(key)

        return class_(*args, **kwargs)
