"""
封装的正则替换
"""

import configparser
import re

from utils.ConfigUtil import my_config


class ParmTemp:
    # 用来存储临时变量
    pass


class MyRegex:
    @staticmethod
    def my_replace(string, content=None, split='#', class_temp=None):
        """
        正则替换
        :param string: 源文本
        :param content: 提供content直接替换功能
        :param split: 替换文本标识符，默认为'#'
        :param class_temp: 如果找不到替换文本，可在此单例中寻找
        :return: 替换完后的新文本
        """
        while split in string:
            pattern = f"{split}(.+?){split}"
            try:
                arg = re.search(pattern, string).group(1)
                word = my_config.get('account', arg)
            except configparser.NoOptionError:
                try:
                    word = content if content is not None else getattr(ParmTemp, arg)
                except AttributeError:
                    word = content if content is not None else getattr(class_temp, arg)
            string = re.sub(pattern, word, string, count=1)
        return string

    @staticmethod
    def my_find(string, pattern):
        """
        正则查找
        :param string: 源文本
        :param pattern: 正则表达式
        :return: 替换完后的新文本
        """
        return re.search(pattern, string).group(1)


myRex = MyRegex()

if __name__ == '__main__':
    list = ['123', None, '2+3']
    for i in list:
        try:
            s = eval(i)
        except TypeError as e:
            s = None
        print(s)
