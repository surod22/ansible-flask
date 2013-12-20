from flask.ext.wtf import Form
from wtforms import TextField, FormField, FieldList
from wtforms.validators import Required
from wtforms.widgets import TableWidget
from wtforms_alchemy import model_form_factory, ModelFieldList
from app.models import Server, Variable

ModelForm = model_form_factory(Form)


class VariableForm(ModelForm):
    class Meta:
        model = Variable


class ServerForm(ModelForm):
    class Meta:
        model = Server

    variables = ModelFieldList(FormField(VariableForm, widget=TableWidget(with_table_tag=False)))