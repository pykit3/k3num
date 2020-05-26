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
```

#   Author

Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>


[pykit3]: https://github.com/pykit3