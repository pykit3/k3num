"""
pk3hunum convert numbers(or numbers in `dict` or `list`) to human readable
format in string.

>>> hunum(103425)
'101.0K'
>>> hunum({ 'total': 10240, 'progress': [1, 1024*2.1, 1024*3.2], })
{'total': '10K', 'progress': ['1', '2.10K', '3.20K']}
>>> parsenum('5.2K')
5324.8
>>> parsenum('10%')
0.1

Attributes:
    value_to_unit(dict): map of int to unit, e.g.: `1024 -> "K"`, `1024² -> "M"`.

        Usage::

            >>> value_to_unit[1024**2]
            'M'

            >>> unit_to_value['K']
            1024

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
