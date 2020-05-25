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
import pk3hunum
print pk3hunum.hunum({
    'total': 10240,
    'progress': [1, 1024*2.1, 1024*3.2],
})
# {"total" : "10K", "progress" : [1, "2.1K", "3.2K"]}
```

#   Author

Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>