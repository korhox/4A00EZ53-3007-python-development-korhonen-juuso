import time


class TimerError(Exception):
    """Timer error handler"""


class Timer:
    def __init__(self):
        self.start_time = 0

    def start(self):
        if self.start_time != 0:
            raise TimerError("Timer already running")
            return False
        else:
            self.start_time = float(time.time())
            return True

    def get_start(self):
        if self.start_time == 0:
            raise TimerError("Timer not running")
            return False
        else:
            return self.start_time

    def get(self):
        if self.start_time == 0:
            raise TimerError("Timer not running")
            return False
        else:
            return float(time.time()) - self.start_time

    def reset(self):
        if self.start_time == 0:
            raise TimerError("Timer not running")
            return False
        else:
            self.start_time = float(time.time())
            return True

    def stop(self):
        if self.start_time == 0:
            raise TimerError("Timer not running")
            return False
        else:
            self.start_time == 0
            return True
