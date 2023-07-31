import datetime
import time
import os
import json
import sys
import traceback
import threading
import typing
from time_log import time_log


def dump_traces():
    for threadId, stack in sys._current_frames().items():
        print(threadId, traceback.extract_stack(stack))
    actives = threading.enumerate()
    print(len(actives))
    for item in actives:
        print(item)


def lambda_all(_list, f) -> bool:
    if not _list:
        return False
    for item in _list:
        if not f(item):
            return False
    return True


def lambda_at_least(_list, f, number):
    if not _list:
        return False
    i = 0
    for item in _list:
        if f(item):
            i += 1
            if i >= number:
                return True
    return False


def map_by_id(lst):
    return dict(zip(map(lambda item: item.id, lst), lst))


def write_json(d: typing.Dict, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=4, ensure_ascii=False, default=str)


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_time(s):
    if s is None:
        return datetime.datetime.now()
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")


def format_time(d: datetime.datetime):
    return d.strftime("%Y-%m-%d %H:%M:%S.%f")


def prefix_id(prefix: str, _id: int):
    return prefix + str(1000 + _id)[1:]


def check_dup_process():
    try:
        id_bytes = str(os.getpid()).encode('utf-8')
        with open('file_locker', mode='xb', buffering=0) as f:
            f.write(id_bytes)
        time_log(f'pid-{os.getpid()}')
    except:
        traceback.print_exc()
        time_log(f'dup_process-{os.getpid()}')
        return time.time() - os.stat('file_locker').st_ctime < 60
    return False


def remove_dup_file():
    try:
        os.remove('file_locker')
    except:
        traceback.print_exc()
