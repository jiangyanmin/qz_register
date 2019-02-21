#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/25


class MaintainInfo:
    def __init__(self, creditcode, captial_currency, captial_amount,
                 captial_unit, corporation, corporation_kind, corporate_institution,
                 enterprise_nature, country_region, region_province, region_city, region_area,
                 credit_rating, telareacode, linktel, other_phone, address, fax, postalcode):
        self.creditcode = creditcode  # 统一社会信用代码
        self.captial_currency = captial_currency  # 注册资本/币种
        self.captial_amount = captial_amount  # 注册资本/金额
        self.captial_unit = captial_unit  # 注册资本/金额单位
        self.corporation = corporation  # 法人代表
        self.corporation_kind = corporation_kind  # 法人类别
        self.corporate_institution = corporate_institution  # 法人机构类别
        self.enterprise_nature = enterprise_nature  # 企业性质
        self.country_region = country_region  # 国别/地区
        self.region_province = region_province  # 行政区域/省
        self.region_city = region_city  # 行政区域/市
        self.region_area = region_area  # 行政区域/区
        self.credit_rating = credit_rating  # 资信等级
        self.telareacode = telareacode  # 联系电话
        self.linktel = linktel
        self.other_phone = other_phone  # 其他联系方式
        self.address = address  # 联系地址
        self.fax = fax  # 传真号
        self.postalcode = postalcode  # 邮政编码

    def set_creditcode(self, creditcode):
        self.creditcode = creditcode
        return self.creditcode

    def get_creditcode(self):
        return self.creditcode

    def set_captial_currency(self, captial_currency):
        self.captial_currency = captial_currency
        return self.captial_currency

    def get_captial_currency(self):
        return self.captial_currency

    def set_captial_amount(self, captial_amount):
        self.captial_amount = captial_amount
        return self.captial_amount

    def get_captial_amount(self):
        return self.captial_amount

    def set_captial_unit(self, captial_unit):
        self.captial_unit = captial_unit
        return self.captial_unit

    def get_captial_unit(self):
        return self.captial_unit

    def set_corporation(self, corporation):
        self.corporation = corporation
        return self.corporation

    def get_corporation(self):
        return self.corporation

    def set_corporation_kind(self, corporation_kind):
        self.corporation_kind = corporation_kind
        return self.corporation_kind

    def get_corporation_kind(self):
        return self.corporation_kind

    def set_corporate_institution(self, corporate_institution):
        self.corporate_institution = corporate_institution
        return self.corporate_institution

    def get_corporate_institution(self):
        return self.corporate_institution

    def set_enterprise_nature(self, enterprise_nature):
        self.enterprise_nature = enterprise_nature
        return self.enterprise_nature

    def get_enterprise_nature(self):
        return self.enterprise_nature

    def set_country_region(self, country_region):
        self.country_region = country_region
        return self.country_region

    def get_country_region(self):
        return self.country_region

    def set_region_province(self, region_province):
        self.region_province = region_province
        return self.region_province

    def get_region_province(self):
        return self.region_province

    def set_region_city(self, region_city):
        self.region_province = region_city
        return self.region_city

    def get_region_city(self):
        return self.region_city

    def set_region_area(self, region_area):
        self.region_area = region_area
        return self.region_area

    def get_region_area(self):
        return self.region_area

    def set_credit_rating(self, credit_rating):
        self.credit_rating = credit_rating
        return self.credit_rating

    def get_credit_rating(self):
        return self.credit_rating

    def set_telareacode(self, telareacode):
        self.telareacode = telareacode
        return self.telareacode

    def get_telareacode(self):
        return self.telareacode

    def set_linktel(self, linktel):
        self.linktel = linktel
        return self.linktel

    def get_linktel(self):
        return self.linktel

    def set_other_phone(self, other_phone):
        self.other_phone = other_phone
        return self.other_phone

    def get_other_phone(self):
        return self.other_phone

    def set_address(self, address):
        self.address = address
        return self.address

    def get_address(self):
        return self.address

    def set_fax(self, fax):
        self.fax = fax
        return self.fax

    def get_fax(self):
        return self.fax

    def set_postalcode(self, postalcode):
        self.postalcode = postalcode
        return self.postalcode

    def get_postalcode(self):
        return self.postalcode