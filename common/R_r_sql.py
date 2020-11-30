# @File   :   R_r_sql.py
# @Author :   July401
# @Date   :   2019/6/15
# @Email  :   july401@qq.com

import pymysql

from common.R_r_config import my_config

"""
输入sql，返回一条或多条
"""


class Mysql:
    def __init__(self, database=None):
        section = 'database'
        host = my_config.get(section, 'host')
        user = my_config.get(section, 'user')
        password = my_config.get(section, 'password')
        database = database
        port = my_config.get(section, 'port')
        charset = my_config.get(section, 'charset')
        self.con = pymysql.connect(host=host, user=user, password=password, database=database, port=eval(port),
                                   charset=charset)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def select(self, sql, resultmode=0):
        """
        封装的select语句
        :param sql: sql语句
        :param resultmode: 0  返回1条，1  返回所有，2  返回4条
        :return: sql查询结果
        """
        self.con.commit()
        self.cur.execute(sql)
        self.con.commit()
        if resultmode == 0:
            temp = self.cur.fetchone()
        elif resultmode == 1:
            temp = self.cur.fetchall()
        elif resultmode == 2:
            temp = self.cur.fetchmany(size=4)
        return temp

    def affect(self, sql):
        self.con.commit()
        temp = self.cur.execute(sql)
        self.con.commit()
        return temp

    def insert(self, sql):
        self.cur.execute(sql)
        self.con.commit()


# my_sql = Mysql()

if __name__ == '__main__':
    sql = f'SELECT leaveamount FROM member where mobilephone = 13912345611'
    res = my_sql.select(sql)
    print(res)
