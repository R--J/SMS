#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Login Controller."""

from flask import request, render_template, Blueprint, redirect, url_for, session, flash
from sms.models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        try:
            user = User.get_user(request.form['stuid'])  # Database
        except BaseException, e:
            print 'Get User Fail: {0}'.format(e)

        if not user:
            print 'Invalid Student ID.'
        elif user.password != request.form['password']:
            print 'Invalid Password.'
        else:
            session['logged_in'] = user.stu_id
            flash('You were logged in')
            return redirect(url_for('auth.userinfo'))
    else:
        if session.get('logged_in'):
            return redirect(url_for('auth.userinfo'))
        return render_template('auth/signin.html')


@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.form
        new_user = User(stu_id=form['stuid'], name=form['name'], password=form['password'], email=form['email'])
        try:
            User.add_user(new_user)  # Database
            return redirect(url_for('auth.signin'))
        except BaseException, e:
            print 'Sign Up Fail: {0}'.format(e)
            return render_template('auth/signup.html')
    else:
        if session.get('logged_in'):
            return redirect(url_for('auth.userinfo'))
        return render_template('auth/signup.html')


@auth.route('/')
def userinfo():
    if not session.get('logged_in'):
        return redirect(url_for('auth.signin'))
    else:
        try:
            stu_id = session.get('logged_in')
            user = User.get_user(stu_id)  # Database
            return render_template('auth/info.html', user=user)
        except BaseException, e:
            print 'Get User Fail: {0}'.format(e)
            return redirect(url_for('auth.signin'))


@auth.route('/signout')
def signout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('auth.signin'))
