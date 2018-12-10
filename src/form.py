from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import ValidationError, DataRequired, EqualTo

from .models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField(
        '重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户已经存在.')


class URIForm(FlaskForm):
    uri = TextField('下载链接', validators=[DataRequired()],
                    render_kw={"placeholder": "支持HTTP、HTTPS、FTP、FTPS、磁力链接等"})
    path = StringField('下载目录')
    submit = SubmitField('提交')


class BTForm(FlaskForm):
    uri = TextField('下载链接', validators=[DataRequired()], render_kw={"placeholder": "test"})
    path = StringField('下载目录', validators=[DataRequired()])
    submit = SubmitField('提交')
