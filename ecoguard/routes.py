from flask import render_template, url_for, redirect
from ecoguard import app, database, bcrypt
from ecoguard.models import Usuario, Protocolo
from flask_login import login_required, login_user, logout_user, current_user
from ecoguard.forms import FormLogin, FormCriarConta, FormProtocolo


@app.route("/", methods=["GET", "POST"])
def index():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("index.html", form=form_login)


@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha, email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    return render_template("perfil.html", usuario=current_user)


@app.route("/protocolo/<id_usuario>", methods=["GET", "POST"])
@login_required
def protocolo(id_usuario):
    form_protocolo = FormProtocolo()
    if form_protocolo.validate_on_submit():
        protocolo = Protocolo(local=form_protocolo.local.data, observacao=form_protocolo.observacao.data, id_usuario=current_user.id)
        database.session.add(protocolo)
        database.session.commit()
        return redirect(url_for("perfil", id_usuario=current_user.id))
    return render_template("protocolo.html", usuario=current_user, form=form_protocolo)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
