#!/usr/bin/python
# -*- coding: utf-8 -*-

#from sms.repository.handler import *
#from sms.models.member import Member
import sys
sys.path.append("../repository")
from handler import *

class User:
    def __init__(self, stu_id, name, password, email, gender=0, phone='', age=0, about_me=None):
        self.stu_id = stu_id
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.phone = phone
        self.age = age
        self.about_me = about_me
        self.members = []

    def schema(self):
        return '(stu_id, name, password, email, gender, phone, age, about_me)'

    def data(self):
        return str(self.stu_id), str(self.name), str(self.password), str(self.email), \
            self.gender, str(self.phone), self.age, str(self.about_me)

    def update(self, password, email, gender, phone, age):
        # args: password, email, gender, phone, age
        field_assign_list = [
            'password=' + password,
            'email=' + email,
            'gender=' + gender,
            'phone=' + phone,
            'age=' + age,
            'about_me=' + about_me
        ]
        field_assign_formatter = ','.join('%s' for _ in field_assign_list)
        condition_formatter = 'stu_id=' + stu_id
        query = """ update {} set {} where {} ; """.format('user', field_assign_formatter, \
            condition_formatter)
        return query_db(query, args=user.data())

    def join_club(self, soc_id, join_data):
        mem = Member(self.stu_id, soc_id, join_data)
        members.push(mem)

    def promote_member(self, member):
        for m in self.members:
            if m.soc_id == member.soc_id:
                if m.level > member.level:
                    member.update(level=level+1)  # level from 0 to 1 for now

    def remove_member(self, member):
        for m in self.members:
            if m.soc_id == member.soc_id:
                if m.level > member.level:
                    member.update(level=level+1)  # level from 0 to 1 for now

    @classmethod
    def add_user(cls, user):
        value_formatter = ','.join('%s' for _ in user.data())
        query = """ insert into {} {} values ({}) ; """.format('user', user.schema(), value_formatter)
        return query_db(query, args=user.data())

    @classmethod
    def get_user_list(cls, soc_id, valid):
        """
        Args: valid - 1 when user is a formal member, 0 when user is applying
        """
        query = """ select stu_id from member where valid = %s AND soc_id = %s  ;"""
        raw_users = query_db(query, args=(valid, soc_id), result_num=-1)
        if raw_users is not None:
            return [cls.get_user_by_id(raw_user) for raw_user in raw_users]
        else:
            return None

    @classmethod
    def get_user_by_id(cls, stu_id):
        query = """ select * from user where stu_id = %s ;"""
        raw_user = query_db(query, args=(stu_id,), result_num=1)
        if raw_user is not None:
            return cls(*raw_user)
        else:
            return None

if __name__ == '__main__':
    us1 = User.get_user_list(1, 0)
    print us1[0].name
    us2 = User.get_user_list(1, 1)
    print us2[0].name