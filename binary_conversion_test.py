import binary_conversion as bc
import pytest

PROPER_DATA = r'23 20 42 79 74 65 2D 63 6F 6D 70 69 6C 65 64'
TRANSLATED = '# Byte-compiled'
IMPROPER_DATA = r'23 20 42 79 74 65 ZZ 63 6F 6D 70 69 6C 65 64'

def test_convert():
    conv = bc.BinConverter()

    data = conv.convert(PROPER_DATA)

    assert data == TRANSLATED

    with pytest.raises(ValueError, match='.*ZZ.*'):
        data = conv.convert(IMPROPER_DATA)
