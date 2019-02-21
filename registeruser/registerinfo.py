#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
# @Author:JiangM
# @Date:2018/9/13


class RegisterInfo:
    def __init__(self, regtype, enttype, entname, password,
                 password2, linkman, linktel, email):
        self._regtype = regtype
        self._enttype = enttype
        self._entname = entname
        self._password = password
        self._password2 = password2
        self._linkman = linkman
        self._linktel = linktel
        self._email = email
        # self._verifyCode = verifyCode

    def set_regtype(self, regtype):
        self._regtype = regtype
        return self._regtype

    def get_regtype(self):
        return self._regtype

    def set_enttype(self, enttype):
        self._enttype = enttype
        return self._enttype

    def get_enttype(self):
        return self._enttype

    def set_entname(self, entname):
        self._entname = entname
        return self._entname

    def get_entname(self):
        return self._entname

    # def set_username(self, username):
    #     self._username = username
    #     return self._username
    #
    # def get_username(self):
    #     return self._username

    def set_password(self, password):
        self._password = password
        return self._password

    def get_password(self):
        return self._password

    def set_password2(self, password2):
        self._password2 = password2
        return self._password2

    def get_password2(self):
        return self._password2

    def set_linkman(self, linkman):
        self._linkman = linkman
        return self._linkman

    def get_linkman(self):
        return self._linkman

    def set_linktel(self, linktel):
        self._linktel = linktel
        return self._linktel

    def get_linktel(self):
        return self._linktel

    def set_email(self, email):
        self._email = email
        return self._email

    def get_email(self):
        return self._email

    # def set_verifyCode(self, verifyCode):
    #     self._verifyCode = verifyCode
    #     return self._verifyCode
    #
    # def get_verifyCode(self):
    #     return self._verifyCode
