from typing import Optional

from ._class import AClass
from ._types import AnEnum


class ExampleException(ValueError):
    """This is a custom exception class."""


def a_public_function(required: int, optional: Optional[str] = None) -> AClass:
    """This is a docstring for the public function.

    This is a multiline comment that checks that things are appended
    together correctly with a space.

    Example:
        ```python
        from example import a_public_function

        obj = a_public_function(100)
        print(obj.enum_value)
        ```

    Arguments:
        required: Something that we need
        optional: This we don't need

    Returns:
        An instance of our fancy class

    Raises:
        ValueError: Actually it doesn't
    """
    return AClass()


def _a_private_function():
    """This should not be visible."""
    pass


__all__ = [
    "a_public_function",
    "AClass",
    "ExampleException",
    "AnEnum",
]
