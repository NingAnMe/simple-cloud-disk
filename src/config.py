import os

from .const import SCP_DIR

SECRET_KEY = 'thisisthetestingsecretkey'
DISK_DIR = 'disk'  # 下载文件的存放路径,可以是绝对路径或者相对程序主目录的路径，默认是disk
ARIA2_POST = 6800
FLV_POST = 6900


class Config(object):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(SCP_DIR, 'scp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
