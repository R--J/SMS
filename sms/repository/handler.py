#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from flask import g
from sms import app
DATABASE = app.config['DATABASE']


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = MySQLdb.connect(
            host=DATABASE['HOST'],
            user=DATABASE['USER'],
            passwd=DATABASE['PASSWD'],
            db=DATABASE['DBNAME']
        )
    return db


def query_db(query, args=(), result_num=-1):
    db = get_db()
    try:
        cursor = db.cursor()

        print 'Excecute: ' + (query % args)
        cursor.execute(query, args)
        if result_num < 0:
            result = cursor.fetchall()
        elif result_num == 1:
            result = cursor.fetchone()
        else:
            result = cursor.fetchmany(result_num)

        cursor.close()

        print 'Commit modifications'
        db.commit()
        return result
    except BaseException, e:
        print 'Executing SQL Error: {0}'.format(e)
        db.rollback()
