import os
import sys
import time

from time_log import time_log
import win_config
from anti_loose import AntiLoose
from utils import py_common_utils
from utils.config_sql_item import sql_executor

sys.path.append('entities')
sys.path.append('utils')
sys.path.append('biz')
if __name__ == '__main__':
    time_log('main is launched')
    if py_common_utils.check_dup_process():
        sys.exit(-1)
    config = win_config.read_json()
    a = AntiLoose(config)
    while a.run():
        time_log('AntiLoose running')
    sql_executor.close()
    py_common_utils.remove_dup_file()
    time_log('quiting main')
