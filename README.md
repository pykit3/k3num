# pk3hunum

[![Build Status](https://travis-ci.com/pykit3/pk3hunum.svg?branch=master)](https://travis-ci.com/pykit3/pk3hunum)
[![Documentation Status](https://readthedocs.org/projects/pk3hunum/badge/?version=stable)](https://pk3hunum.readthedocs.io/en/stable/?badge=stable)

Convert number to human readable format in a string.

# Install

```
pip install pk3hunum
```

# Synopsis

```python
>>> hunum(103425)
'101.0K'
>>> hunum({ 'total': 10240, 'progress': [1, 1024*2.1, 1024*3.2], })
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