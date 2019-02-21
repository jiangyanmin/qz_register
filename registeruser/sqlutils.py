#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author: JiangM
# @Date:2018/9/12
# import pymysql 支持Mysql
import pymssql  # 支持sql server
import re
from registeruser.sqlcmdtextstore import SqlCmdTextStore


def read_data_from_db():
    conn = SqlDBUtil(
        '192.168.102.91',
        'sa',
        'Hymake@123',
        'qztender2',
        1433
    )
    conn.connect()
    # test_data = conn.query_first_line(SqlCmdTextStore.query_first_line_sql_info(RegisterInfo.get_linktel()))
    test_data = conn.query_first_line(SqlCmdTextStore.query_first_line_sql_info('11111111111'))
    msg = test_data[0]
    patt = re.compile(r'[0-9]{6}')
    verifyCode = re.findall(patt, msg)[0]
    conn.close()
    # test_data = SqlDBUtil.query_first_line(SqlCmdTextStore.query_first_line_sql_info('18259480185'))
    # print(verifyCode)
    return verifyCode


class SqlDBUtil:
    def __init__(self, host, username, password, db_name, port):
        self._host_ip = host
        self._username = username
        self._password = password
        self._db_name = db_name
        self._host_port = port

        self._db = None
        self._cursor = None

    # 连接数据库
    def connect(self):
        if self._db is None:
            try:
                self._db = pymssql.connect(
                    self._host_ip, self._username, self._password,
                    self._db_name, self._host_port, charset="utf8"
                )
               # print(self._db.open)
            except Exception as e:
                print(e)
        if self._cursor is None:
            try:
                self._cursor = self._db.cursor()
                # self._cursor = Connection.cursor()
            except NameError:
                print("数据库连接失败")#数据库连接失败的异常处理
            else:
                # print(self._cursor)
                pass

            # raise(NameError, "数据库连接失败")
            # self._cursor = self._db.cursor()
        else:
            # print(self._cursor)
            pass

    # #获取查询结果集的第一行
    def query_first_line(self, sql_cmd_text):
        self._cursor.execute(sql_cmd_text)
        first_line_result = self._cursor.fetchone()
        # print(first_line_result)
        return first_line_result

    # #关闭游标，关闭数据库连接
    def close(self):
        if self._db is not None:
            if self._cursor is True:
                try:
                    self._cursor.close()
                    self._db.close()
                # except Exception as e:
                #   print(e)
                except:
                    pass

if __name__ == '__main__':
#     # sql_db = SqlDBUtil(
#     #     '192.168.102.91',
#     #     'sa',
#     #     'Hymake@123',
#     #     'qztender2',
#     #     1433
#     # )
#     # sql_db.connect()
#     # sql_db.query_first_line(SqlCmdTextStore.query_first_line_sql_info('18259480185'))
#     # sql_db.close()
    read_data_from_db()
