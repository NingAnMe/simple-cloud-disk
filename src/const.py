import os

from .config import DISK_DIR

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
SCP_DIR = os.path.dirname(SRC_DIR)

# 如果没有配置DOSK_DIR，则设置为默认值
if not DISK_DIR:
    DISK_DIR = 'disk'
