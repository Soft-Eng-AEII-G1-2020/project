import file_management as fm
import os
import shutil


F_NAME1 = 'fontawesome-webfont'
F_NAME2 = 'OpenSans-Regular'
F_NAMEOUT = 'test-out'
ROOTDIR = './exemplaryFiles/'
EXTENSION = '.bin'
TESTOUT = './out/'
TESTDATA = '''
test data test data test data
test data test data test data
test data test data test data
test data test data test data
test data test data test data
test data test data test data
test data test data test data
test data test data test data
'''


def test_load_file():
    bf = fm.BinFile()

    bf.load_file(ROOTDIR + F_NAME1 + EXTENSION)

    assert len(bf.readList) == 1

    assert bf.readList[0][2] == F_NAME1 + EXTENSION

    assert bf.readList[0][0] == F_NAME1


def test_load_folder():
    bf = fm.BinFile()

    bf.load_folder(ROOTDIR)

    assert len(bf.readList) == 2

    matrix = sorted([F_NAME1, F_NAME2])

    for i in range(0, 2):
        assert bf.readList[i][2] == matrix[i] + EXTENSION
        assert bf.readList[i][0] == matrix[i]

    assert len(bf.readList) == bf.get_file_count() == 2


def is_single_file_test():
    bf = fm.BinFile()

    bf.load_file(ROOTDIR + F_NAME1 + EXTENSION)

    assert bf.is_single_file()

    bf.load_folder(ROOTDIR)

    assert bf.is_single_file() == False


def test_reset():
    bf = fm.BinFile()

    bf.load_folder(ROOTDIR)

    bf.reset()

    assert len(bf.readList) == 0


def test_saving():
    bf = fm.BinFile()

    bf.load_folder(ROOTDIR)

    if not os.path.exists(TESTOUT):
        os.makedirs(TESTOUT)

    bf.save_file_by_index(TESTOUT, 0, TESTDATA, F_NAMEOUT)

    with open(TESTOUT + F_NAMEOUT + '.txt') as f:
        data = f.read()

        assert data == TESTDATA

    shutil.rmtree(TESTOUT, ignore_errors=True)
