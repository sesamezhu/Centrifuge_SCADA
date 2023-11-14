import sys

from anti_loose import AntiLoose
from cv_tools import py_common_utils, win_config
from cv_tools.time_log import time_log

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
        time_log(f'AntiLoose run {a.loop_no} times')
    time_log('quiting main')
