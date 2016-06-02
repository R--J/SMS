#!/usr/bin/python
# -*- coding: utf-8 -*-

class Activity:
	def __init__(self, title, abstract=None, content, level,
		publisher_id, start_time, end_time=None, soc_id):
		self.title = title
		self.abstract = abstract
		self.content = content
		self.level = level
		self.publisher_id = publisher_id
		self.start_time = start_time
		self.end_time = end_time
		self.soc_id = soc_id
	