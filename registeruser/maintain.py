#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/25
from registeruser.parserexcelinfo import parser_excel_info
from registeruser.maintaininfo import MaintainInfo
from selenium import webdriver


# 把从excel读取出的完善信息用例嵌套列表转换成行读取出来
def convert_maintain_to_list():
    # 获取所有用例数据列表
    maintain_data_info_list = parser_excel_info('registertestcase.xlsx', 'Mantain', 5, 6)
    every_maintain_data_list = []  # 列表，存储获取每一行用例数据
    for i in range(len(maintain_data_info_list)):
        creditcode = maintain_data_info_list[i][0]
        scanning_copy = maintain_data_info_list[i][1]
        captial_currency = maintain_data_info_list[i][2]
        captial_amount = maintain_data_info_list[i][3]
        captial_unit = maintain_data_info_list[i][4]
        corporation = maintain_data_info_list[i][5]
        corporation_kind = maintain_data_info_list[i][6]
        corporate_institution = maintain_data_info_list[i][7]
        enterprise_nature = maintain_data_info_list[i][8]
        region = maintain_data_info_list[i][9]
        credit_rating = maintain_data_info_list[i][10]
        tel = maintain_data_info_list[i][11]
        other_phone = maintain_data_info_list[i][12]
        address = maintain_data_info_list[i][13]
        fax = maintain_data_info_list[i][14]
        postalcode = maintain_data_info_list[i][15]
        maintain_info = MaintainInfo(creditcode, captial_currency, captial_amount,
                 captial_unit, corporation, corporation_kind, corporate_institution,
                 enterprise_nature, country_region, region_province, region_city, reginon_area,
                 credit_rating, telareacode, linktel, other_phone, address, fax, postalcode)
        every_maintain_data_list.append(maintain_info)
    return every_maintain_data_list


class Maintain:
    def __init__(self):
        pass

    def setUP(self):
        self.ieDriver = webdriver.Ie(executable_path='C:\Program Files\Internet Explorer\IEDriverServer.exe')
        self.ieDriver.maximize_window()
        # self.chromeDriver = webdriver.Chrome(
        # executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        # self.chromeDriver.maximize_window()
        # self.chromeDriver.get('http://59.57.251.156:9100/qztender/abframe/auth/login.jsp')

    def tearDown(self):
        self.ieDriver.quit()

    def maintain(self, entname):
        for n in range(len(convert_maintain_to_list())):
            self.ieDriver.get('http://59.57.251.156:9100/qztender/website/org.gocom.'
                          'abframe.auth.Login.flow?_eosFlowAction=login&acOperator/'
                          'usertype=gov&acOperator/userid=%s&acOperator/password=mWtn+'
                          'OUaT7Y4g9C0SpJzzg==&acOperator/flag=1' % entname)





