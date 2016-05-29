#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

HOST = 'localhost'
USER = 'root'
PASSWD = ''
DB = 'sms_db'

ADD_ACTION = 'add_act'
DEL_ACTION = 'del_act'
QUERY_ACTION = 'query_act'
MODIFY_ACTION = 'modify_act'

def access_repo(table, action, index, i, field, f):
	"""Define four operations on the repository.

	Args:
        table (str): name of table accessed.
        action (str): operation on repo.
        index (str): field uesd to find the tuple.
        i (str): value of the filed that uesd to find the tuple.
        field (str): field to be modified.
        f (str): new value of the field to be modified.
    """

	con = MySQLdb.connect(HOST, USER, PASSWD, DB)
	cur = con.cursor()

	if action == ADD_ACTION:
		# todo
		pass
	elif action == DEL_ACTION:
		# todo
		pass
	elif action == QUERY_ACTION:
		# todo
		pass
	elif action == MODIFY_ACTION:
		sql = "UPDATE %s SET %s = %s WHERE %s = %s" % \
		(table, field, f, index, i)
	
	try:
		# Execute the SQL command
		print 'Execute: ' + sql
		cur.execute(sql)
		# Commit your changes in the database
		print 'Commit modifications'
		con.commit()
	except:
		print 'Executing SQL Error'
		# Rollback in case there is any error
		con.rollback()

	con.close()