import os

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from . import app, db
from .form import LoginForm, RegistrationForm
from .models import User, Job
from .utils import delete_admin, get_disk_main_dir, get_dirs_files


@app.route('/')
def index():
    return render_template('index.html', title='主页')


@app.route('/disk', methods=['GET', 'POST'])
@login_required
def disk():
    disk_main_dir = get_disk_main_dir()
    if not os.path.isdir(disk_main_dir):
        os.makedirs(disk_main_dir)
    dirs, files = get_dirs_files(disk_main_dir)

    print(disk_main_dir)
    print(dirs)
    print(files)
    return render_template('disk.html', title='网盘', dirs=dirs, files=files)


@app.route('/uri', methods=['GET', 'POST'])
@login_required
def uri():
    disk_main_dir = get_disk_main_dir()
    if not os.path.isdir(disk_main_dir):
        os.makedirs(disk_main_dir)
    dirs, files = get_dirs_files(disk_main_dir)

    print(disk_main_dir)
    print(dirs)
    print(files)
    return render_template('uri.html', title='链接下载', dirs=dirs, files=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    账号登录
    :return:
    """
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
    """
    账号注册
    :return:
    """
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
        flash('创建管理员账号成功，请记住账号密码!')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route('/logout')
def logout():
    """
    退出登录
    :return:
    """
    logout_user()
    return redirect(url_for('index'))


@app.shell_context_processor
def make_shell_context():
    """
    添加Flask Shell环境
    :return:
    """
    return {'db': db, 'User': User, 'Job': Job, 'delete_admin': delete_admin, }
