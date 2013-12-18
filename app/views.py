from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.validators import Required
from app.forms import NewServerForm
from app.models import Server
from flask import render_template, request, redirect
from app import app, db


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
    form = NewServerForm()
    if form.validate_on_submit():
        new_server = Server(form.name.data)
        db.session.add(new_server)
        db.session.commit()
        return redirect('/servers')
    return render_template('new_server.html', form=form)

@app.route('/servers/<server_id>/edit', methods=['GET', 'POST'])
def edit(server_id):
    EditServerForm = model_form(Server, base_class=Form, field_args={'name': {'validators': [Required('Server name cannot be blank.')]}})
    server = Server.query.filter_by(id=server_id).first_or_404()
    form = EditServerForm(request.form, server)
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


