# -*- coding: utf-8 -*-
# @File   :   auto_dict.py
# @Author :   julystone
# @Date   :   2019/8/28 9:59
# @Email  :   july401@qq.com


class _AutoDict(dict):
    def __init__(self):
        self._res = {}

    def __setitem__(self, key, val):
        self._res[key] = val
        dict.__setitem__(self, key, val)

    def __getitem__(self, key):
        if key in self._res.keys():
            return self._res[key]
        else:
            r = _AutoDict()
            self.__setitem__(key, r)
            return r


class _DictObj(dict):
    pass


def dict_to_object(dic):
    if isinstance(dic, dict) is False:
        return dic
    inst = _DictObj
    for key, value in dic.items():
        setattr(inst, str(key), value)
    return inst


if __name__ == '__main__':
    dic = {"aa": 1, "bb": 2}
    res = dict_to_object(dic)
    print(res.aa)
    print(res.bb)
