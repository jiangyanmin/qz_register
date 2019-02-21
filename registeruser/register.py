#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/13
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from registeruser.sqlutils import read_data_from_db
from time import sleep
from registeruser.sqlcmdtextstore import SqlCmdTextStore
from registeruser.registerinfo import RegisterInfo
from registeruser.parserexcelinfo import parser_excel_info
from registeruser.maintaininfo import MaintainInfo
import logging
import os
import random



# 把从excel读取出的注册用例嵌套列表转换成行读取出来
def convert_register_to_list():
    # 获取所有用例数据列表
    register_data_info_list = parser_excel_info('registertestcase.xlsx', 'Register', 5, 6)
    every_register_data_list = []  # 列表，存储获取每一行用例数据
    for i in range(len(register_data_info_list)):
        regtype = register_data_info_list[i][0]
        enttype = register_data_info_list[i][1]
        entname = register_data_info_list[i][2]
        password = register_data_info_list[i][3]
        password2 = register_data_info_list[i][4]
        linkman = register_data_info_list[i][5]
        linktel = register_data_info_list[i][6]
        email = register_data_info_list[i][7]
        register_info = RegisterInfo(regtype, enttype, entname, password,
                                           password2, linkman, linktel, email)
        every_register_data_list.append(register_info)
    return every_register_data_list


# 把从excel读取出的完善信息用例嵌套列表转换成行读取出来
def convert_maintain_to_list():
    # 获取所有用例数据列表
    maintain_data_info_list = parser_excel_info('registertestcase.xlsx', 'Mantain', 5, 6)
    every_maintain_data_list = []  # 列表，存储获取每一行用例数据
    for i in range(len(maintain_data_info_list)):
        creditcode = maintain_data_info_list[i][0]
        # scanning_copy = maintain_data_info_list[i][1]
        captial_currency = maintain_data_info_list[i][1]
        captial_amount = maintain_data_info_list[i][2]
        captial_unit = maintain_data_info_list[i][3]
        corporation = maintain_data_info_list[i][4]
        corporation_kind = maintain_data_info_list[i][5]
        corporate_institution = maintain_data_info_list[i][6]
        enterprise_nature = maintain_data_info_list[i][7]
        country_region = maintain_data_info_list[i][8]
        region_province = maintain_data_info_list[i][9]
        region_city = maintain_data_info_list[i][10]
        region_area = maintain_data_info_list[i][11]
        credit_rating = maintain_data_info_list[i][12]
        telareacode = maintain_data_info_list[i][13]
        linktel = maintain_data_info_list[i][14]
        other_phone = maintain_data_info_list[i][15]
        address = maintain_data_info_list[i][16]
        fax = maintain_data_info_list[i][17]
        postalcode = maintain_data_info_list[i][18]
        maintain_info = MaintainInfo(creditcode, captial_currency, captial_amount,
                 captial_unit, corporation, corporation_kind, corporate_institution,
                 enterprise_nature, country_region, region_province, region_city, region_area,
                 credit_rating, telareacode, linktel, other_phone, address, fax, postalcode)
        every_maintain_data_list.append(maintain_info)
    return every_maintain_data_list


class Register:
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
        # self.ieDriver.close()

    def register(self):
        for n in range(len(convert_register_to_list())):
            self.ieDriver.get(
                'http://59.57.251.156:9100/qztender/website/com.hymake.fjbid.website.register.flow?_eosFlowAction=qy')
            sleep(2)
            regtype_name = convert_register_to_list()[n].get_regtype()
            enttype_name = convert_register_to_list()[n].get_enttype()
            for handle in self.ieDriver.window_handles:
                self.ieDriver.switch_to_window(handle)
                if regtype_name == '建设工程':
                    self.regtype_jsgc = self.ieDriver.find_element_by_id('register_typeradio0').click()
                    if enttype_name == '招标代理机构':
                        self.enttype_zbdl = self.ieDriver.find_element_by_id('enterprise_type1radio0').click()
                    elif enttype_name == '招标人':
                        self.enttype_zbr = self.ieDriver.find_element_by_id('enterprise_type1radio1').click()
                    elif enttype_name == '投标人':
                        self.enttype_tbr = self.ieDriver.find_element_by_id('enterprise_type1radio2').click()
                elif regtype_name == '政府采购':
                    self.regtype_zgcg = self.ieDriver.find_element_by_id('register_typeradio1').click()
                    if enttype_name == '采购人':
                        self.enttype_cgr = self.ieDriver.find_element_by_id('enterprise_type2radio0').click()
                    elif enttype_name == '采购代理机构':
                        self.enttype_cgdl = self.ieDriver.find_element_by_id('enterprise_type2radio1').click()
                    elif enttype_name == '供应商':
                        self.enttype_gys = self.ieDriver.find_element_by_id('enterprise_type2radio2').click()
                elif regtype_name == '产权交易':
                    self.regtype_cqjy = self.ieDriver.find_element_by_id('register_typeradio2').click()
                    if enttype_name == '出让人':
                        self.enttype_crr = self.ieDriver.find_element_by_id('enterprise_type3radio0').click()
                    elif enttype_name == '受让人':
                        self.enttype_srr = self.ieDriver.find_element_by_id('enterprise_type3radio1').click()
                self.entname = self.ieDriver.find_element_by_id('enterprise_name').send_keys(
                    convert_register_to_list()[n].get_entname())
                # self.username = self.ieDriver.find_element_by_id('userid').send_keys(
                #     convert_register_to_list()[n].get_username())
                self.password = self.ieDriver.find_element_by_id('password').send_keys(
                    convert_register_to_list()[n].get_password())
                self.password2 = self.ieDriver.find_element_by_id('pwd').send_keys(
                    convert_register_to_list()[n].get_password2())
                self.linkman = self.ieDriver.find_element_by_id('reportliable').send_keys(
                    convert_register_to_list()[n].get_linkman())
                self.linktel = self.ieDriver.find_element_by_id('enterprise_regtel').send_keys(
                    convert_register_to_list()[n].get_linktel())
                self.email = self.ieDriver.find_element_by_id('enterprise_email').send_keys(
                    convert_register_to_list()[n].get_email())
                self.getCode = self.ieDriver.find_element_by_css_selector('#sendMsg>.button').click()  # 点击“免费获取验证码”
                self.codeImg = self.ieDriver.find_element_by_id('codeImg').get_attribute('value')  # 获取附加码值
                self.code = self.ieDriver.find_element_by_id('FJverifyCode').send_keys(self.codeImg)  # 输入附加码值
                # 点击‘获取验证码’
                self.sendCode = self.ieDriver.find_elements_by_class_name('button')[1].click()
                # 输入验证码
                self.verifyCode = self.ieDriver.find_element_by_id('verifyCode').send_keys(read_data_from_db())
                self.agree = self.ieDriver.find_element_by_id('agree').click()  # 点击接受服务协议
                self.ieDriver.execute_script('document.getElementsByTagName("img")[10].click()')
                logging.info('%s注册成功' % convert_register_to_list()[n].get_entname())
                # logging.info('%s注册成功' % convert_register_to_list()[n].get_entname())
                WebDriverWait(self.ieDriver, 500, 0.5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, '点此登录系统')))
                self.mantain_login = self.ieDriver.find_element_by_link_text('点此登录系统').click()
                # sleep(3)
                WebDriverWait(self.ieDriver, 500, 0.5).until(
                    EC.presence_of_element_located((By.NAME, 'topFrame')))
                # self.login_name = self.ieDriver.find_element_by_xpath('//*[@id="right1"]/table tr[2]/td/span').text
                self.ieDriver.switch_to_frame('topFrame')
                sleep(2)
                self.login_name = self.ieDriver.find_element_by_xpath(
                    '//span[contains(text(), "欢迎")]').text
                    # '#right1>table>tbody>tr:nth-child(2)>td>span').text
                self.register_name = convert_register_to_list()[n].get_entname()
                if self.register_name in self.login_name:
                    logging.info('%s登录成功' % convert_register_to_list()[n].get_entname())
                    self.ieDriver.find_element_by_link_text('企业管理').click()
                    self.ieDriver.switch_to_default_content()
                    self.ieDriver.switch_to_frame('bodyFrame_all')
                    self.ieDriver.switch_to_frame('bodyFrame')
                    # self.ieDriver.find_element_by_xpath('//input[contains(@value, "编辑")').click()
                    self.ieDriver.find_element_by_css_selector(
                        'tr.form_bottom>td:nth-child(1)>input:nth-child(1)').click()
                    # 统一社会信用代码
                    self.ieDriver.find_element_by_id('creditcode').send_keys(
                        convert_maintain_to_list()[0].get_creditcode())
                    # 三证合一
                    # self.ieDriver.find_element_by_css_selector(
                    #     'tr#creditcodeTR>td:nth-child(2) tr:nth-child(2) td:nth-child(2)>input').send_keys('三证合一.jpg')
                    # self.ieDriver.find_element_by_xpath(
                    #     "//td[text(),'三证合一扫描件']/following-sibling::td/input").click()
                    # self.ieDriver.find_element_by_css_selector(
                    #     'tr#creditcodeTR>td[2]>table tr[2]>td[2]>input').click()
                    sleep(2)
                    self.ieDriver.find_element_by_xpath('//form[@name="dataForm"]//tr[@id="creditcodeTR"]/td[2]//tr[2]input[1]').click()
                    # self.ieDriver.find_element_by_css_selector(
                    #     'tr#creditcodeTR>td:nth-child(2) tr:nth-child(2) td:nth-child(2)>input').click()  # 上传
                    # self.ieDriver.find_element_by_id('imgCE').click()
                    # sleep(2)
                    #
                    # self.ifr_ele = self.ieDriver.find_element_by_class_name('eos-popwin-body-iframe')
                    # self.ieDriver.switch_to_frame(self.ifr_ele)  # 跳转到iframe(class)
                    # # self.ieDriver.find_element_by_css_selector('#flashContainer>#imgUploadFlash').click()
                    # # self.mouse = self.ieDriver.find_element_by_css_selector('#popupControls>a')
                    # # ActionChains(self.ieDriver).move_to_element(self.mouse).click().perform()
                    # # sleep(10)
                    # os.system('D:\上传图片2.exe')
                    # sleep(5)
                    #
                    # self.ieDriver.find_element_by_id('imgUpload').click()
                    # self.ieDriver.find_element_by_id('closwin').click()
                    # self.ieDriver.switch_to_default_content()
                    # 有效时间
                    self.ieDriver.find_element_by_id('isCQYX').click()
                    # 选择币种
                    if convert_maintain_to_list()[n].get_captial_currency() == '人民币':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/moneytype"] option:nth-child(1)').click()
                    elif convert_maintain_to_list()[n].get_captial_currency() == '美元':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/moneytype"] option:nth-child(2)').click()
                    else:
                        raise Exception('无法找到输入的币种')
                    self.ieDriver.find_element_by_id('capitalauthid').send_keys(
                        convert_maintain_to_list()[n].get_captial_amount())  # 填写注册资本金额
                    # 选择资金单位
                    if convert_maintain_to_list()[n].get_captial_unit() == '元':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/priceunit"]>option:nth-child(1)').click()
                    elif convert_maintain_to_list()[n].get_captial_unit() == '美元':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/priceunit"]>option:nth-child(2)').click()
                    else:
                        raise Exception('无法找到输入的资金单位')
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/entcharge"]').send_keys(
                        convert_maintain_to_list()[n].get_corporation()
                    )
                    # 选择法人类型
                    if convert_maintain_to_list()[n].get_corporation_kind() == '自然人':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/biddercodetype"]>option:nth-child(2)').click()
                    elif convert_maintain_to_list()[n].get_corporation_kind() == '法人':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/biddercodetype"]>option:nth-child(3)').click()
                    elif convert_maintain_to_list()[n].get_corporation_kind() == '其他':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/biddercodetype"]>option:nth-child(4)').click()
                    else:
                        raise Exception('无法找到输入的法人类别')

                    # 选择法人机构类别
                    if convert_maintain_to_list()[n].get_corporate_institution() == '企业':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/legaltype"]>option:nth-child(2)').click()
                    elif convert_maintain_to_list()[n].get_corporate_institution() == '机关法人':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/legaltype"]>option:nth-child(3)').click()
                    elif convert_maintain_to_list()[n].get_corporate_institution() == '事业单位':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/legaltype"]>option:nth-child(4)').click()
                    elif convert_maintain_to_list()[n].get_corporate_institution() == '社会组织':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/legaltype"]>option:nth-child(5)').click()
                    elif convert_maintain_to_list()[n].get_corporate_institution() == '其他':
                        self.ieDriver.find_element_by_css_selector(
                            'select[name="enterprise/legaltype"]>option:nth-child(6)').click()
                    else:
                        raise Exception('无法找到输入的法人机构类别')

                    # 选择企业性质
                    # self.ieDriver.find_element_by_xpath('//input[@onclick="getEntproperty();"]') .click()
                    # self.ieDriver.find_element_by_xpath(
                    #     '//input[@name="enterprise/entpropertyShow"]/following-sibling::input[2]').click()
                    if convert_maintain_to_list()[n].get_enterprise_nature() == '国有全资':
                        # self.ieDriver.find_element_by_xpath(
                        #     '//span[contains(text(), "国有全资")]').click()
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('国有全资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '集体全资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('集体全资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '股份合作':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('股份合作')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '国有联营':
                        # self.ieDriver.find_element_by_xpath(
                        #     '//span[contains(text(), "国有联营")]').click()
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('国有联营')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '集体联营':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('集体联营')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '国有与集体联营':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('国有与集体联营')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他联营':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他联营')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '有限责任（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('有限责任（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他有限责任（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他有限责任（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '股份有限（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('股份有限（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '私有独资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('私有独资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '私有合伙':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('私有合伙')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '私营有限责任（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('私营有限责任（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '私营股份有限（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('私营股份有限（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '个体经营':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('个体经营')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他私有':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他私有')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他内资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他内资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '内地和港、澳或台合资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('内地和港、澳或台合资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '内地和港、澳或台合作':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('内地和港、澳或台合作')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '港、澳或台独资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('港、澳或台独资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '港、澳或台投资股份有限（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('港、澳或台投资股份有限（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他港澳台投资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他港澳台投资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '中外合资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('中外合资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '中外合作':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('中外合作')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '外资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('外资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '国外投资股份有限（公司）':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('国外投资股份有限（公司）')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他国外投资':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他国外投资')
                    elif convert_maintain_to_list()[n].get_enterprise_nature() == '其他':
                        self.ieDriver.execute_script(
                            'document.getElementById("entproperty").removeAttribute("readOnly");')
                        self.ieDriver.find_element_by_id('entproperty').send_keys('其他')
                    else:
                        raise Exception('无法找到输入的企业性质')
                    # self.ieDriver.find_element_by_css_selector('div>input[value="确定"]').click()

                    # 选择国别/地区
                    if convert_maintain_to_list()[n].get_country_region() == '中华人民共和国':
                        self.ieDriver.find_element_by_xpath(
                            'select[name="enterprise/county"]>option:nth-child(2)').click()
                    elif convert_maintain_to_list()[n].get_country_region() == '香港':
                        self.ieDriver.find_element_by_css_selector(
                             'select[name="enterprise/county"]>option:nth-child(3)').click()
                    elif convert_maintain_to_list()[n].get_country_region() == '台湾省':
                        self.ieDriver.find_element_by_css_selector(
                             'select[name="enterprise/county"]>option:nth-child(4)').click()
                    else:
                        raise Exception('无法找到输入的国别/地区')

                    # 选择行政区域（写死福建省厦门市思明区）
                    if convert_maintain_to_list()[n].get_region_province() == '福建省':
                        self.ieDriver.find_element_by_id('provinceid_input').clear()
                        self.ieDriver.find_element_by_id('provinceid_input').send_keys('福建省')
                        # self.ieDriver.find_element_by_xpath('//*[contains(text(), "福建省")').click()
                    else:
                        raise Exception('请输入“福建省”')
                    if convert_maintain_to_list()[n].get_region_city() == '厦门市':
                        # self.ieDriver.find_element_by_xpath(
                        #     '//nobr[contains(text(), "厦门市")]').click()
                        self.ieDriver.find_element_by_id('cityid_input').clear()
                        self.ieDriver.find_element_by_id('cityid_input').send_keys('厦门市')
                    else:
                        raise Exception('请输入“厦门市”')
                    if convert_maintain_to_list()[n].get_region_area() == '思明区':
                        # self.ieDriver.find_element_by_xpath(
                        #     '//nobr[contains(text(), "思明区")]').click()
                        self.ieDriver.find_element_by_id('countyid_input').clear()
                        self.ieDriver.find_element_by_id('countyid_input').send_keys('思明区')
                    else:
                        raise Exception('请输入“思明区”')

                    # 行业代码
                    # self.ieDriver.find_element_by_xpath('//label[@id="testlabel"]/following-sibling::input[1]').click()
                    # self.industry_code1 = self.ieDriver.find_element_by_name('select1')
                    # Select(self.industry_code1).select_by_index(random.randint(0, 19))
                    # self.industry_code2 = self.ieDriver.find_element_by_name('select2')
                    # self.option_len = len(self.industry_code2.find_element_by_tag_name('option'))
                    # Select(self.industry_code2).select_by_index(random.randint(0, self.option_len-1))
                    # self.ieDriver.find_element_by_css_selector('tr.form_bottom>td>input[value="确 定"]').click()
                    self.ieDriver.find_element_by_id('returnValue').clear()
                    self.ieDriver.find_element_by_id('returnValue').send_keys('I65')

                    # 资信等级
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/creditgrade"]').send_keys(
                        convert_maintain_to_list()[n].get_credit_rating()
                    )
                    # 联系电话
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/telareacode"]').send_keys(
                        convert_maintain_to_list()[n].get_telareacode()
                    )
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/linktel"]').send_keys(
                        convert_maintain_to_list()[n].get_linktel()
                    )
                    # 其他联系方式
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/otherlinkway"]').send_keys(
                        convert_maintain_to_list()[n].get_other_phone()
                    )
                    # 联系地址
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/linkadd"]').send_keys(
                        convert_maintain_to_list()[n].get_address()
                    )
                    # 传真
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/taxtel"]').send_keys(
                        convert_maintain_to_list()[n].get_fax()
                    )
                    # 邮编
                    self.ieDriver.find_element_by_css_selector('input[name="enterprise/postcode"]').send_keys(
                        convert_maintain_to_list()[n].get_postalcode()
                    )

                    # 保存并提交
                    self.ieDriver.find_element_by_xpath('//input[@value="保存并提交"]').click()
                    self.ieDriver.switch_to_default_content()
                else:
                    raise('%s登录失败' % convert_register_to_list()[n].get_entname())
                    pass


                # self.ieDriver.quit()


if __name__ == '__main__':
    reg = Register()
    # reg.read_data_from_db()
    reg.setUP()
    reg.register()
    # reg.tearDown()
    # excel_info_list = parser_excel_info('registertestcase.xlsx', 'Register', 5, 6)
    # re_list = []
    # for i in range(len(excel_info_list)):
    #     regtype = excel_info_list[i][0]
    #     enttype = excel_info_list[i][1]
    #     entname = excel_info_list[i][2]
    #     password = excel_info_list[i][3]
    #     password2 = excel_info_list[i][4]
    #     linkman = excel_info_list[i][5]
    #     linktel = excel_info_list[i][6]
    #     email = excel_info_list[i][7]
    #     re = RegisterInfo(regtype, enttype, entname, password,
    #                  password2, linkman, linktel, email)
    #     re_list.append(re)
    # print(re_list[0].get_regtype())
    # print(len(convert_register_to_list()))
    # print(convert_register_to_list()[1].get_enttype())

