import time


class Timer:
    def __init__(self):
        self.start_time = 0

    def start(self):
        if self.start_time != 0:
            raise Exception("Timer already running")
            return False
        else:
            self.start_time = float(time.time())
            return True

    def get_start(self):
        if self.start_time == 0:
            raise Exception("Timer not running")
            return False
        else:
            return self.start_time

    def get(self):
        if self.start_time == 0:
            raise Exception("Timer not running")
            return False
        else:
            return float(time.time()) - self.start_time

    def reset(self):
        self.start_time = 0
        return True

    def stop(self):
        if start_time == 0:
            raise Exception("Timer not running")
            return False
        else:
            self.start_time == 0
            return True
