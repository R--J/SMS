#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Society Controller."""

from flask import request, render_template, Blueprint, redirect, url_for, session, flash
from sms.models.user import User

auth = Blueprint('auth', __name__)

@society.route('/cresociety/', methods=['GET', 'POST'])
def create_society():
    if request.method == 'POST':
        form = request.form
        new_society = Society(name=form['name'], about_us=form['about_us'], \
            tutor=form['tutor'], founder=form['founder'], president=['president'])
        try:
            Society.add_society(new_society)  # Database
            return redirect(url_for('society_control.create_society'))
        except BaseException, e:
            print 'Sign Up Fail: {0}'.format(e)
            return render_template('auth/signup.html')
    else:
        if session.get('logged_in'):
            return redirect(url_for('auth.userinfo'))
        return render_template('auth/signup.html')

