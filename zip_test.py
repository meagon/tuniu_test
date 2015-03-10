
#-*- coding:utf-8 -*-

import sys

py_version = sys.version_info
py_3k = py_version >= (3, 0, 0)
py_2k = py_version <= (2, 8, 0)

def zip_check(filename):
    check = False

    if py_3k:
        import codecs
        zip_file = codecs.open(filename, 'r', encoding="ascii")
    else:  # python 2
        zip_file = open(filename, 'r')

    mark = zip_file.read(2)
    if mark == 'PK':
        check = True
    return check

def test():
    import zipfile
    filename = 'test.zip'
    _file = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    _file.write(sys.argv[0])
    _file.close()
    ok_file = zip_check(filename)
    print(ok_file)

if __name__ == '__main__':
    test()
