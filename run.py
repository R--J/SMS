#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Activate App."""

from sms import app

app.run(host='0.0.0.0', port=8080, debug=False)


from sms.models.user import User
u = User.get_user_by_id('13331047')
u.update(['1212', '1@q.com', 'male', '110', '21'])
