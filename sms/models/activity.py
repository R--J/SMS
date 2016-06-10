#!/usr/bin/python
# -*- coding: utf-8 -*-


class Activity:
	def __init__(self, title, abstract, content, level, publisher_id, start_time, end_time, soc_id, \
		participant_no):
		self.title = title
		self.abstract = abstract
		self.content = content
		self.level = level
		self.publisher_id = publisher_id
		self.start_time = start_time
		self.end_time = end_time
		self.soc_id = soc_id
		self.participant_no = participant_no
	
	def schema(self):
		return '(title, abstract, abstract, content, level, publisher_id, start_time, end_time, soc_id, \
			participant_no)'

	def data(self):
		return str(self.title), str(self.abstract), str(self.content), \
			str(self.level), str(self.publisher_id), str(self.start_time), \
			str(self.end_time), self.soc_id, self.participant_no

	def update(self, name, founded_data, tutor, founder, president, total_no, valid):
		field_assign_list = [
			'title=' + title,
			'abstract=' + abstract,
			'content=' + content,
			'level=' + level,
			'publisher_id=' + publisher_id,
			'start_time=' + start_time,
			'end_time=' + end_time,  # valid can only be updated by admin
			"participant_no=" + participant_no
		]
		field_assign_formatter = ','.join('%s' for _ in field_assign_list)
		condition_formatter = 'soc_id=' + soc_id
		query = """ update {} set {} where {} ; """.format('activity', field_assign_formatter, condition_formatter)
		return query_db(query, args=user.data())

	@classmethod
	def add_activity(cls, activity):
		value_formatter = ','.join('%s' for _ in user.data())
		query = """ insert into {} {} values ({}) ; """.format('activity', user.schema(), value_formatter)
		return query_db(query, args=activity.data())

	@classmethod
	def get_activity_list(cls, soc_id):
		query = """ select * from activity where soc_id = %s ordered by end_time desc;"""
		raw_activities = query_db(query, args=(soc_id,), result_num=-1)
		if raw_activities is not None:
			return [cls.get_activity_by_id(raw_activity) for raw_activity in raw_activities]
		else:
			return None

	@classmethod
	def get_activity_by_id(cls, id):
		query = """ select * from activity where id = %s;"""
		raw_activity = query_db(query, args=(id,), result_num=1)
		if raw_activity is not None:
			return cls(*raw_activity)
		else:
			return None
