#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/21
from ddt import ddt, data, unpack
from registeruser.parserexcelinfo import parser_excel_info


@ddt
class TestRegisterCase1:
   @data(*parser_excel_info('registertestcase.xlsx', 'Register', 5, 6))
   @unpack
   def test_data_from_register(self, regtype, enttype, entname, password,
                               password2, linkman, linktel, email):
       print(regtype)

