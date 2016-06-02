#!/usr/bin/python
# -*- coding: utf-8 -*-

from sms.repository.handler import *


class User:
    def __init__(self, stu_id, name, password, email, gender=0, phone='', age=0):
        self.stu_id = stu_id
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.phone = phone
        self.age = age

    def schema(self):
        return '(stu_id, name, password, email, gender, phone, age)'

    def data(self):
        return str(self.stu_id), str(self.name), str(self.password), str(self.email), self.gender, str(self.phone), self.age

    @classmethod
    def add_user(cls, user):
        value_formatter = ','.join('%s' for _ in user.data())
        query = """ insert into {} {} values ({}) ; """.format('user', user.schema(), value_formatter)
        return query_db(query, args=user.data())

    @classmethod
    def get_user(cls, stu_id):
        query = """ select * from user where stu_id = %s ;"""
        raw_user = query_db(query, args=(stu_id,), result_num=1)
        if raw_user is not None:
            return cls(*raw_user)
        else:
            return None
