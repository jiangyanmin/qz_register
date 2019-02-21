#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author: JiangM
# @Date:2018/9/12


class SqlCmdTextStore:
    @staticmethod
    def query_first_line_sql_info(phone_number):
        sql_cmd_text = "select msg from HT_SMS where phone=%s ORDER BY create_dt DESC" % phone_number
        return sql_cmd_text

    @staticmethod
    def delete_register_sql_info(user):
        sql_reg_text = "DELETE HY_REGISTERS where entid=(select entid from ac_operator where userid=%s)" % user
        sql_ent_text = "DELETE HT_ENTERPRISE_TEMP where entname=%s" % user
        sql_ope_text = "delete ac_operator where userid=%s" % user
        return sql_reg_text, sql_ent_text, sql_ope_text
