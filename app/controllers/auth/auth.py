#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Login Controller."""

from flask import request
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.models.user import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
