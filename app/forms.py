from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class NewServerForm(Form):
    name = TextField('name', [Required('All fields are required.')])