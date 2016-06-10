#!/usr/bin/python
# -*- coding: utf-8 -*-


class Member:
    def __init__(self, stu_id, soc_id, join_data, member_info, level=0, valid=0):

        self.stu_id = stu_id
        self.soc_id = soc_id
        self.join_data = join_data
        self.member_info = member_info
        self.level = level
        self.valid = valid

    def update(self, level, valid):
        field_assign_list = [
            'member_info=' + member_info,
            'level=' + level,
            'valid=' + valid
        ]
        field_assign_formatter = ','.join('%s' for _ in field_assign_list)
        condition_formatter = 'stu_id=' + stu_id +', soc_id=' + soc_id
        query = """ update {} set {} where {} ; """.format('member', \
            field_assign_formatter, condition_formatter)
        return query_db(query, args=user.data())

