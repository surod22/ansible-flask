from app.yml_output import create_yml
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.validators import Required
from app.forms import ServerForm, VariableForm
from app.models import Server, Variable
from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.yml_output import create_yml


@app.route('/')
def home():
    return redirect('/servers')

@app.route('/servers/<server_id>')
def show(server_id):
    server = Server.query.filter_by(id=server_id).first_or_404()
    return render_template('show_server.html', server=server)

@app.route('/servers')
def index():
    servers = Server.query.all()
    return render_template('servers.html', servers=servers)

@app.route('/servers/new', methods=['GET', 'POST'])
def new():
    new_server = Server()
    variable = Variable()
    variable_form = VariableForm(obj=variable)
    form = ServerForm(request.form, obj=new_server)
    if form.add_variable.data:
            form.variables.append_entry(variable_form)
    elif form.delete_variable.data and len(form.variables.entries) > 1:
            form.variables.pop_entry()
    elif form.validate_on_submit():
        if form.create_server.data:
            form.populate_obj(new_server)
            db.session.add(new_server)
            db.session.commit()
            create_yml()
            return redirect('/servers')
    return render_template('new_server.html', form=form)

@app.route('/servers/<server_id>/edit', methods=['GET', 'POST'])
def edit(server_id):
    server = Server.query.filter_by(id=server_id).first_or_404()
    form = ServerForm(request.form, server)
    if form.validate_on_submit():
        form.populate_obj(server)
        name_exist = Server.query.filter_by(name=form.name.data).first()
        if name_exist:
            form.name.errors.append('Server name is already taken.')
        else:
            db.session.commit()
            return redirect('/servers')
    return render_template('edit_server.html', form=form, server=server)

@app.route('/servers/<server_id>/delete', methods=['POST'])
def delete(server_id):
    server = Server.query.get(server_id)
    db.session.delete(server)
    db.session.commit()
    return redirect('/servers')

# @app.route('/servers/edit', methods=['GET', 'POST'])
# def modify():
#     servers = Server.query.all()
#     form = ProjectForm(request.form, servers)
#
#     return render_template('edit_all.html', form=form, servers=servers)


