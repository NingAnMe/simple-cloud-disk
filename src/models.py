from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login


class User(UserMixin, db.Model):
    """
    UserMixin提供了如下方法：
    is_authenticated: 一个用来表示用户是否通过登录认证的属性，用True和False表示。
    is_active: 如果用户账户是活跃的，那么这个属性是True，否则就是False。
    is_anonymous: 常规用户的该属性是False，对特定的匿名用户是True。
    get_id(): 返回用户的唯一id的方法，返回值类型是字符串(Python 2下返回unicode字符串).
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    jobs = db.relationship('Job', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.username)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Job {} {}>'.format(self.id, self.uri)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
