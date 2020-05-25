"""
pk3hunum convert numbers(or numbers in `dict` or `list`) to human readable
format in string.

Attributes:
    value_to_unit(dict): map of int to unit, e.g.: `1024 -> "K"`, `1024² -> "M"`.

    unit_to_value(dict): reverse map of `value_to_unit`.

"""

from .hunum import (
    K,
    M,
    G,
    T,
    P,
    E,
    Z,
    Y,
    hunum,
    parsenum,
    parseint,

    value_to_unit,
    unit_to_value,
)

__version__ = '0.1.0'
_name = 'pk3hunum'

__all__ = [
    'K',
    'M',
    'G',
    'T',
    'P',
    'E',
    'Z',
    'Y',
    'hunum',
    'parsenum',
    'parseint',

    'value_to_unit',
    'unit_to_value',
]
