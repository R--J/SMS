#!/usr/bin/python
# -*- coding: utf-8 -*-

from repo_accessor import access_repo

def add_member(Member):
	# todo
	pass

def del_member(Member):
	# todo
	pass

def query_member(Member):
	# todo
	pass

def promote_member(Member):
	access_repo('member', 'modify_act', 'stu_id', Member.stu_id, 'level', 0)
