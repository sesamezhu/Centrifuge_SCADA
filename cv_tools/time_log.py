import logging.config
import datetime
import threading
import os
import sys
import time
from typing import overload

previous_map = {0: time.time()}

if not os.path.exists("logs"):
    print(os.makedirs("logs"))
logging.config.fileConfig('configs/logging.conf')
console_log = logging.getLogger('cout')
console_log.setLevel(10)
time_logger = logging.getLogger('time')
time_logger.setLevel(10)


class DualLogger:
    def __init__(self):
        self.terminal = sys.__stdout__
        self.logger = console_log

    def write(self, message):
        if not message:
            return
        if message in ["\r", "\n", "\r\n"]:
            return
        if str.isspace(message):
            self.terminal.write(message)
            return
        self.console(message)
        self.log(message)

    def flush(self):
        self.terminal.flush()

    def console(self, message):
        stamp = datetime.datetime.now().strftime('%H:%M:%S.%f')
        thread = threading.current_thread().name
        self.terminal.write(f"{stamp}::{thread}::{message}\n")

    @overload
    def log(self, message) -> None:
        ...


class DebugLogger(DualLogger):
    def __init__(self):
        super().__init__()

    def log(self, message):
        self.logger.debug(message)


class InfoLogger(DualLogger):
    def __init__(self):
        super().__init__()
        self.logger = time_logger

    def log(self, message):
        self.logger.info(message)


class ErrLogger(DualLogger):
    def __init__(self):
        super().__init__()
        self.terminal = sys.__stderr__

    def log(self, message):
        self.logger.error(message)


debug_logger = DebugLogger()
info_logger = InfoLogger()
error_logger = ErrLogger()
sys.stdout = debug_logger
sys.stderr = error_logger


def now_compact():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d_%H%M%S.%f')


def time_err(s):
    time_key(s, error_logger)


def time_log(s):
    time_key(s, info_logger)


def get_elapse() -> float:
    _time = time.time()
    _key = threading.get_ident()
    previous_log = previous_map.get(_key, _time)
    previous_map[_key] = _time
    return _time - previous_log


def time_key(s, file=sys.stdout):
    if s is None:
        return
    elapse = get_elapse()
    file.write(f"{elapse:1.3f}--{s}")
