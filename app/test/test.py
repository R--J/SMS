#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This test example is to test the promote_member funciton.
"""

import sys
sys.path.append('../models')
sys.path.append('../controllers')

from member import Member
from member_management import promote_member
import repo_accessor

m = Member('13331046')
promote_member(m)
