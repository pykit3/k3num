#!/usr/bin/env python
# coding: utf-8


class Hex(str):
    """
    Create a `str` based instance that represents a fixed-length hex string,
    to simplify hex and arithmetic operations.

    An `Hex` instance supports arithmetic operations: `+ - * / % **`.

    NOTE: **it overrides native `str` operation such as `str + str`**.

    Args:

        data: can be a `str`, `int` or tuple in form of `(<prefix_hex>, <filling_byte>)`

        byte_length:
            specifies number of bytes for this hex.
            It can not be changed after creating it.

            > byte length x 2 = hex length

            It also can be a symblic name: `crc32`, `md5`, `sha1` or `sha256`.


    Attributes:
        hex (str): a plain string of hex `'00000102'`.
        bytes (bytes): a plain string of bytes `b'\0\0\1\2'`.
        int (int): a int value `0x0102` same as `int('00000102', 16)`.
        byte_length (int): number of bytes in `Hex.bytes`.
    """

    byte_length = None

    lengths = dict(
        crc32=4,
        md5=16,
        sha1=20,
        sha256=32,
    )

    def __new__(clz, data, byte_length=None):

        if byte_length is None:
            byte_length = clz.byte_length

            assert byte_length is not None

        if isinstance(byte_length, str):
            # convert named length to number
            b = byte_length.lower()
            byte_length = clz.lengths[b]

        if isinstance(data, (list, tuple)):
            data, fillwith = data

            assert isinstance(fillwith, int)
            assert 0 <= fillwith <= 0xff
            assert isinstance(data, str)
            assert len(data) % 2 == 0

            data += ('%02x' % fillwith) * (byte_length - len(data) // 2)

        if isinstance(data, int):
            if data < 0:
                raise ValueError('int/long must be positive but: ' + repr(data))

            data = '%0{n}x'.format(n=byte_length * 2) % data

        if not isinstance(data, str):
            raise TypeError('exptect str or int/long, but: ' + str(type(data)))

        if len(data) == byte_length * 2:
            # new from hex string
            _hex = data
        elif len(data) == byte_length:
            _hex = data.encode('utf-8').hex()
        else:
            raise ValueError('str data length must be {l2} for hex,'
                             ' or {l} for byte,'
                             ' but: {act}'.format(
                                 l=byte_length,
                                 l2=byte_length * 2,
                                 act=len(data)))

        _bytes = bytes.fromhex(_hex)
        _long = int(_hex, 16)

        x = super(Hex, clz).__new__(clz, _hex)
        x.hex = _hex
        x.bytes = _bytes
        x.int = _long
        x.byte_length = byte_length

        return x

    def __add__(self, b):
        return self._arithm(self.int + self._tolong(b))

    def __sub__(self, b):
        return self._arithm(self.int - self._tolong(b))

    def __mul__(self, b):
        return self._arithm(self.int * self._tolong(b))

    def __truediv__(self, b):
        return self._arithm(self.int // self._tolong(b))

    def __floordiv__(self, b):
        return self._arithm(self.int // self._tolong(b))

    def __mod__(self, b):
        return self._arithm(self.int % self._tolong(b))

    def __pow__(self, b):
        return self._arithm(self.int ** self._tolong(b))

    def _tolong(self, x):
        if isinstance(x, self.__class__):
            return x.int
        elif isinstance(x, int):
            return x
        else:
            raise TypeError(str(type(self)) + ' does not support arithmetic operation with {b}'.format(b=repr(x)))

    def _arithm(self, x):
        if x < 0:
            x = 0

        if x >= 256 ** self.byte_length:
            x = 256 ** self.byte_length - 1

        return self.__class__(x, self.byte_length)

    def __str__(self):
        return self.hex

    @classmethod
    def crc32(clz, data): return clz(data, 'crc32')

    @classmethod
    def md5(clz, data): return clz(data, 'md5')

    @classmethod
    def sha1(clz, data): return clz(data, 'sha1')

    @classmethod
    def sha256(clz, data): return clz(data, 'sha256')
