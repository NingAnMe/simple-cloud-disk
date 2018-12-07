import os

from .config import DISK_DIR, SECRET_KEY

SRC_DIR = os.path.abspath(os.path.dirname(__file__))  # simple could disk 项目目录
SCP_DIR = os.path.dirname(SRC_DIR)  # 程序源码目录

# 如果没有配置DOSK_DIR，则设置为默认值disk
if not DISK_DIR:
    DISK_DIR = 'disk'


class Config(object):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(SCP_DIR, 'scp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
