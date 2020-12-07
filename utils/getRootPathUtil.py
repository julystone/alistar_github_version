import os


def getRootPath():
    rootPath = os.path.dirname(os.path.dirname(__file__))
    return rootPath


if __name__ == '__main__':
    res = getRootPath()
    print(res)
