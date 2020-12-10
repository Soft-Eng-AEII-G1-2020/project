import file_management as fm
import binary_conversion as bc
import pytest
import datetime

PROPER_DATA = r'00100011 00100000 01000010 01111001 01110100 01100101 00101101 01100011 01101111 01101101 01110000 01101001 01101100 01100101 01100100'
IMPROPER_DATA = r'00100012 00100000 01000010 01111001 01110100 01100101 00101101 01100011 01101111 01101101 01110000 01101001 01101100 01100101 01100100'
HEX = r'23 20 42 79 74 65 2D 63 6F 6D 70 69 6C 65 64 '
DEC = r'035 032 066 121 116 101 045 099 111 109 112 105 108 101 100 '
OCT = r'043 040 102 171 164 145 055 143 157 155 160 151 154 145 144 '
ASCII = r'# Byte-compiled'

FILEPATH = './exemplaryFiles/OpenSans-Regular.bin'


def test_convert():
    conv = bc.BinConverter()

    out = [ASCII, HEX, DEC, OCT]

    for i in range(0, 4):
        data = conv.convert(PROPER_DATA, i)

        assert data == out[i]

        with pytest.raises(ValueError, match='.*2.*'):
            data = conv.convert(IMPROPER_DATA, i)


def test_time():
    conv = bc.BinConverter()
    bf = fm.BinFile()

    start = datetime.datetime.now().timestamp()

    bf.load_file(FILEPATH)

    data = bf.get_read_file_content_by_index(0)
    data = ' '.join('{:08b}'.format(c) for c in data)
    data = data.encode('ascii').decode('unicode-escape')

    conv.convert(data, 0)

    end = datetime.datetime.now().timestamp()

    assert end - start <= 5
