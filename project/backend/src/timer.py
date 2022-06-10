import time

start_time = 0


def start():
    if start_time != 0:
        raise Exception("Timer already running")
        return False
    else:
        start_time = float(time.time())
        return True


def get_start():
    if start_time == 0:
        raise Exception("Timer not running")
        return False
    else:
        return start_time


def get():
    if start_time == 0:
        raise Exception("Timer not running")
        return False
    else:
        return float(time.time()) - start_time


def reset():
    if start_time == 0:
        raise Exception("Timer not running")
        return False
    else:
        start_time = float(time.time())
        return True


def stop():
    if start_time == 0:
        raise Exception("Timer not running")
        return False
    else:
        start_time == 0
        return True
