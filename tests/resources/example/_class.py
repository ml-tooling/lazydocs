from ._types import AnEnum


class AClass:
    """This is a docstring for the class."""
    def __init__(self):
        pass

    def enum_value(self) -> AnEnum:
        """This is a method that returns an enumeration value."""
        return AnEnum.FIRST
