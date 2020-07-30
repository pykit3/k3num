# k3num

[![Build Status](https://travis-ci.com/pykit3/k3num.svg?branch=master)](https://travis-ci.com/pykit3/k3num)
[![Documentation Status](https://readthedocs.org/projects/k3num/badge/?version=stable)](https://k3num.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3num)](https://pypi.org/project/k3num)

Convert number to human readable format in a string.

k3num is a component of [pykit3] project: a python3 toolkit set.


# Install

```
pip install k3num
```

# Synopsis

```python
>>> readable(103425)
'101.0K'
>>> readable({ 'total': 10240, 'progress': [1, 1024*2.1, 1024*3.2], })
{'total': '10K', 'progress': ['1', '2.10K', '3.20K']}
>>> parsenum('5.2K')
5324.8
>>> parsenum('10%')
0.1
>>> value_to_unit[1024**2]
'M'
>>> unit_to_value['K']
1024
>>> Hex(0x0102, 4)
'00000102'
>>> Hex(0x0102, 'crc32')
'00000102'
>>> Hex.crc32(0x0102)
'00000102'
>>> Hex('00000102', 'crc32')
'00000102'
>>> Hex.crc32('00000102')
'00000102'
>>> Hex(('12', 1), 'crc32')
'12010101'
>>> Hex(0x0102, 'crc32') + 1
'00000103'
>>> Hex(0x0102, 'crc32') * 2
'00000204'
>>> Hex(0x0102, 'crc32') - 1000000
'00000000'
>>> Hex(0x0102, 'crc32') * 1000000000
'ffffffff'
>>> Hex.sha1(0) + Hex.sha1(('10', 0))
'1000000000000000000000000000000000000000'
>>> Hex.sha1(0) + Hex.sha1(('10', 0)) * 2
'2000000000000000000000000000000000000000'
```

#   Author

Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>


[pykit3]: https://github.com/pykit3