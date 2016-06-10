#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sys
# sys.path.append("../repository")
# from handler import *

class Society:
	def __init__(self, soc_id, name, about_us, founded_data, tutor=None,
		founder='Unknown', president='Empty Now', total_no=1, valid=0):
		self.soc_id = soc_id
		self.name = name
		self.about_us = about_us
		self.founded_data = founded_data
		self.tutor = tutor
		self.founder = founder
		self.president = president
		self.total_no = total_no
	
	def schema(self):
		return '(name, about_us, founded_data, tutor, founder, president, total_no, valid)'

	def data(self):
		return str(self.name), str(self.about_us), str(self.founded_data), \
			str(self.tutor), str(self.founder), str(self.president), self.total_no, self.valid

	def update(self, name, founded_data, tutor,
		founder, president, total_no, valid):
		field_assign_list = [
			'about_us=' + about_us,
			'founded_data=' + founded_data,
			'tutor=' + tutor,
			'founder=' + founder,
			'president=' + president,
			'total_no=' + total_no,
			'valid=' + valid  # valid can only be updated by admin
		]
		field_assign_formatter = ','.join('%s' for _ in field_assign_list)
		condition_formatter = 'soc_id=' + soc_id
		query = """ update {} set {} where {} ; """.format('society', field_assign_formatter, condition_formatter)
		return query_db(query, args=user.data())

	@classmethod
	def add_society(cls, society):
		value_formatter = ','.join('%s' for _ in user.data())
		query = """ insert into {} {} values ({}) ; """.format('society', user.schema(), value_formatter)
		return query_db(query, args=society.data())

	@classmethod
	def get_society_list(cls, valid):
		query = """ select soc_id from society where valid = %s ;"""
		raw_societies = query_db(query, args=(valid,), result_num=-1)
		if raw_societies is not None:
			return [cls.get_society_by_id(raw_society) for raw_society in raw_societies]
		else:
			return None

	@classmethod
	def get_society_by_id(cls, soc_id):
		query = """ select * from society where soc_id = %s;"""
		raw_society = query_db(query, args=(soc_id,), result_num=1)
		if raw_society is not None:
			return cls(*raw_society)
		else:
			return None

	
if __name__ == '__main__':
	s1 = Society.get_society_list(0)
	for _s in s1:
		print _s.name, _s.about_us, _s.founded_data
	s2 = Society.get_society_list(1)
	for _s in s2:
		print _s.name, _s.about_us, _s.founded_data

