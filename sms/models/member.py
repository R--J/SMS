#!/usr/bin/python
# -*- coding: utf-8 -*-


class Member:
    def __init__(self, stu_id, soc_id, level):
        self.stu_id = stu_id
        self.soc_id = soc_id
        self.level = level

    @classmethod
    def add_member(cls, member):
        # todo
        pass

    @classmethod
    def del_member(cls, member):
        # todo
        pass

    @classmethod
    def query_member(cls, member):
        # todo
        pass

    @classmethod
    def promote_member(cls, member):
        # access_repo('member', 'modify_act', 'stu_id', Member.stu_id, 'level', 0)
        pass
