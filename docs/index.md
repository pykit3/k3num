# k3num

[![Action-CI](https://github.com/pykit3/k3num/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3num/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3num/badge/?version=stable)](https://k3num.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3num)](https://pypi.org/project/k3num)

Human-readable number formatting and hex string utilities.

k3num is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3num
```

## Quick Start

### Human-readable Number Formatting

```python
from k3num import readable, parsenum

# Convert numbers to human-readable format
readable(103425)
# '101.0K'

readable({'total': 10240, 'progress': [1, 1024*2.1, 1024*3.2]})
# {'total': '10K', 'progress': ['1', '2.10K', '3.20K']}

# Parse human-readable strings back to numbers
parsenum('5.2K')
# 5324.8

parsenum('10%')
# 0.1
```

### Hex String Utilities

```python
from k3num import Hex

# Create hex strings with specific byte lengths
Hex(0x0102, 4)
# '00000102'

Hex(0x0102, 'crc32')
# '00000102'

# Arithmetic operations on hex strings
Hex(0x0102, 'crc32') + 1
# '00000103'

Hex(0x0102, 'crc32') * 2
# '00000204'
```

## API Reference

::: k3num

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
