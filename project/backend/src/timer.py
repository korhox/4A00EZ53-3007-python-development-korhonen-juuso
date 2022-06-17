import time


class Timer:
    """Creates a timer object for timing"""

    def __init__(self):
        """Initiates the default variables"""
        self.start_time = 0

    def start(self):
        """Starts the timer

        Raises:
            Exception: describing the error

        Returns:
            bool: True on success, None on failure"""
        if self.start_time != 0:
            raise Exception("Timer already running")
            return None
        else:
            self.start_time = float(time.time())
            return True

    def get_start(self):
        """Get the starting time of the timer

        Raises:
            Exception: describing the error

        Returns:
            int: the starting time of the timer, None on error 
        """
        if self.start_time == 0:
            raise Exception("Timer not running")
            return None
        else:
            return self.start_time

    def get(self):
        """Get the time of the current timer

        Raises:
            Exception: describing the error

        Returns:
            int: the time of the timer, None on error 
        """
        if self.start_time == 0:
            raise Exception("Timer not running")
            return None
        else:
            return float(time.time()) - self.start_time

    def reset(self):
        """Reset the timer to zero"""
        self.start_time = 0

    def stop(self):
        """Stops the timer without resetting the timer

        Raises:
            Exception: describing the error

        Returns:
            bool: True on success, False on error
        """
        if start_time == 0:
            raise Exception("Timer not running")
            return False
        else:
            self.start_time == 0
            return True
