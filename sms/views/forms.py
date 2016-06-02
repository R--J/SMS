from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class SignUpForm(Form):
    stu_id = TextField('Student Id', [Required(message='Must provide a stu_id.')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])
    name = TextField('Email Address', [Required(message='Forgot your email address?')])
    email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])


class SignInForm(Form):
    pass
