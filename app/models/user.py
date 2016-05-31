#!/usr/bin/python
# -*- coding: utf-8 -*-

class User:
	def __init__(self, stu_id, name, password,
		email, gender, phone=None, age=None):
		self.stu_id = stu_id
		self.name = name
		self.password = password
		self.email = email
		self.gender = gender
		self.phone = phone
		if age is None:
			self.age = 0
		else:
			self.age = age
