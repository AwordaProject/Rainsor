from typing import Type, TypeVar


T_Saved = TypeVar("T_Saved")


class Saver:
    space: dict = {}

    def __init__(self) -> None:
        pass

    def save(self, name: str, value):
        if name in self.space:
            raise KeyError("This thing have already saved")
        self.space[name] = value

    def get(self, name: str, type: Type[T_Saved]) -> T_Saved:
        if name not in self.space:
            raise KeyError("Where have this?")
        if isinstance(self.space[name], type):
            raise ValueError(" Type unmatch")
        return self.space[name]

    def modify(self, name: str, value):
        if name not in self.space:
            raise KeyError("Where have this?")
        self.space[name] = value

    def del_it(self, name):
        self.space.pop(name)
