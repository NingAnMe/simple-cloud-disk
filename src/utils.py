import os

from . import db
from .form import User
from .const import SCP_DIR, DISK_DIR


def delete_admin():
    """
    删除管理员账号
    :return:
    """
    users = User.query.all()
    for u in users:
        db.session.delete(u)
    db.session.commit()


def get_disk_main_dir():
    """
    获取网盘主目录
    :return:
    """
    if os.path.isabs(DISK_DIR):
        download_dir = DISK_DIR
    else:
        download_dir = os.path.join(SCP_DIR, DISK_DIR)
    return download_dir


def get_dirs_files(path):
    """
    获取指定目录的路径
    :param path:
    :return:
    """
    files_found = os.listdir(path)
    files_found.sort()
    dirs = list()
    files = list()
    for f in files_found:
        f_abs = os.path.join(path, f)
        if os.path.isdir(f_abs):
            dirs.append(f)
        elif os.path.isfile(f_abs):
            files.append(f)
    return dirs, files
