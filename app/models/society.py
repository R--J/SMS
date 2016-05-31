#!/usr/bin/python
# -*- coding: utf-8 -*-

class Society:
	def __init__(self, name, founded_data, tutor=None,
		founder='Unknown', president, total_no=1):
		self.name = name
		self.founded_data = founded_data
		self.tutor = tutor
		self.founder = founder
		self.president = president
		self.total_no = total_no
	