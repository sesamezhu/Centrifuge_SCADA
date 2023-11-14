import json
import os
import socket
import traceback
import threading
import math
import typing
from datetime import datetime
from typing import Iterable

import numpy
import torch

from cv_tools.win_config import json_grid


def print_alive():
    actives = threading.enumerate()
    print("alive_threads", len(actives), actives)


def lambda_all(_list, f) -> bool:
    if not _list:
        return False
    for item in _list:
        if not f(item):
            return False
    return True


def lambda_at_least(_list: Iterable, f, number=1):
    if not _list:
        return False
    i = 0
    for item in _list:
        if f(item):
            i += 1
            if i >= number:
                return True
    return False


def lambda_run(_list: Iterable, f):
    for item in _list:
        f(item)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def fetch_field(row, no):
    return None if row is None else row[no]


def to_cpu(tensor):
    return tensor.cpu().tolist()  # .numpy()


def float_cpu(tensor):
    return tensor.float().cpu().tolist()  # .numpy()


def to_gpu(data: numpy.ndarray, gpu=''):
    return torch.Tensor(data).to(gpu).float() / 255.


CHECK_DUP_SOCKET = None


def check_dup_process(port: int):
    try:
        global CHECK_DUP_SOCKET
        CHECK_DUP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CHECK_DUP_SOCKET.bind(('127.0.0.1', port))
        CHECK_DUP_SOCKET.listen()
    except:
        traceback.print_exc()
        return True
    return False


def download_path():
    dt = datetime.now()
    path = f"download/{dt.hour:0=2}{dt.minute:0=2}"
    os.makedirs(path, exist_ok=True)
    return path


def image_path():
    dt = datetime.now()
    path = f"{json_grid['image_root']}\\{dt.year}{dt.month:0=2}{dt.day:0=2}\\{dt.hour:0=2}"
    os.makedirs(path, exist_ok=True)
    return path


def map_by_id(lst):
    return dict(zip(map(lambda item: item.id, lst), lst))


def write_json(d: typing.Dict, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=4, ensure_ascii=False, default=str)


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
