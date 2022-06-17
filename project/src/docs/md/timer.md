Module timer
============

Classes
-------

`Timer()`
:   Creates a timer object for timing
    
    Initiates the default variables

    ### Methods

    `get(self)`
    :   Get the time of the current timer
        
        Raises:
            Exception: describing the error
        
        Returns:
            int: the time of the timer, None on error

    `get_start(self)`
    :   Get the starting time of the timer
        
        Raises:
            Exception: describing the error
        
        Returns:
            int: the starting time of the timer, None on error

    `reset(self)`
    :   Reset the timer to zero

    `start(self)`
    :   Starts the timer
        
        Raises:
            Exception: describing the error
        
        Returns:
            bool: True on success, None on failure

    `stop(self)`
    :   Stops the timer without resetting the timer
        
        Raises:
            Exception: describing the error
        
        Returns:
            bool: True on success, False on error