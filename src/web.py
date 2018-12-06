from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from . import app, db
from .form import LoginForm, RegistrationForm
from .models import User, Job


@app.route('/')
def index():
    return render_template('index.html', title='主页')


@app.route('/disk', methods=['GET', 'POST'])
@login_required
def disk():
    files = None
    return render_template('disk.html', title='网盘', files=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('disk'))
    users = User.query.all()
    if not users:
        return redirect(url_for('register'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('disk')
        return redirect(next_page)
    return render_template('login.html', title='登录', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('disk'))

    users = User.query.all()
    if users:
        flash('已经创建管理员账号!')
        return redirect(url_for('register'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，请记住账号密码!')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def delete_admin():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
    db.session.commit()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Job': Job, 'delete_admin': delete_admin, }
