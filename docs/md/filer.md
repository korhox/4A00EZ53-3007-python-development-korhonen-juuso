Module filer
============

Functions
---------

    
`add_word(word: str)`
:   Adds a word
    
    Args:
        word (string): Word to be added

    
`get_all_words()`
:   Gets all words from words.txt
    
    Returns:
        string: All the words from words.txt

    
`get_word()`
:   Returns a random word from the word list
    
    Returns:
        str: Random word

    
`read(file: str)`
:   Reads the file in given path
    
    Args:
        file (string): The path to the file to be read
    
    Returns:
        string: The file content, empty string on error

    
`remove_word(index: int)`
:   Removes a word by its index number
    
    Args:
        index (int): An index of the word to be removed

    
`reset_words()`
:   

    
`save_wordlist(wordlist: list = ['umbrella', 'computer', 'programmer', 'apple', 'mac', 'doorbell', 'paper', 'usb', 'speaker', 'mouse', 'printer', 'lamp', 'camera', 'webcam', 'remote', 'microphone', 'desk', 'stool', 'clock', 'bill', 'magnet', 'microsoft', 'facebook', 'discord', 'slack', 'game', 'steam', 'ubisoft', 'window', 'file', 'directory', 'desktop', 'trackpad', 'headpohones', 'keyboard'])`
:   Saves the entire wordlist replacing the old one
    
    Args:
        wordlist (list, optional): _description_. Defaults to default_wordlist.split(",").

    
`word_exists(word: str)`
:   Chec whether the word exists or not
    
    Args:
        word (str): a word to be checked
    
    Returns:
        bool: True when word exists, False when not