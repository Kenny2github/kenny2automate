from typing import Optional, TypeVar

T = TypeVar('T')

class AttrDict:
    def __init__(self, attrs: dict[str, T]):
        self.__dict__.update(attrs)
    def __getitem__(self, key: str) -> T:
        return self.__dict__[key]
    def __setitem__(self, key: str, value: T):
        self.__dict__[key] = value
    def __repr__(self) -> str:
        return repr(self.__dict__)
    def __str__(self) -> str:
        return str(self.__dict__)
    def get(self, key: str, default: T = None) -> Optional[T]:
        return self.__dict__.get(key, default)