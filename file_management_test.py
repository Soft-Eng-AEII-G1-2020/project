import pytest
import file_management as fm


def test_load_file():
    bf = fm.BinFile()

    bf.load_file('./exemplaryFiles/fontawesome-webfont.bin')

    assert len(bf.readList) == 1

    assert bf.readList[0][2] == 'fontawesome-webfont.bin'

    assert bf.readList[0][0] == 'fontawesome-webfont'


def test_load_files():
    bf = fm.BinFile()

    bf.load_folder('./exemplaryFiles/')

    assert len(bf.readList) == 2

    matrix = ['fontawesome-webfont', 'OpenSans-Regular']

    for i in range(0, 2):
        assert bf.readList[i][2] == matrix[i] + '.bin'
        assert bf.readList[i][0] == matrix[i]


def is_single_file_test():
    bf = fm.BinFile()

    bf.load_file('./exemplaryFiles/fontawesome-webfont.bin')

    assert bf.is_single_file()

    bf.load_folder('./exemplaryFiles/')

    assert bf.is_single_file() == False
