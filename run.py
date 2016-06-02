#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Activate App."""

from sms import app
app.run(host='0.0.0.0', port=8080, debug=True)
