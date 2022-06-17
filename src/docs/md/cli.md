Module cli
==========

Functions
---------

    
`clear()`
:   Clears the CLI

    
`create_header(title: str)`
:   Creates beautiful header with ascii game name and title
    
    Args:
        title (string): the title to be added in to the header
    
    Returns:
        string: the header

    
`create_menu(items: list)`
:   creates menu from a list of titles
    
    Args:
        items (list): list of strings, each string is one menu item
    
    Returns:
        string: _description_

    
`format_input(title: str = 'Press enter to return main menu', options: int = 0, subtitle: str = '↩')`
:   Formats input
    
    The default subtitle is different depending on amount of options. Subtitle parameter overrides this behavior.
        if options == 0: subtitle = "↩"
        if options == 1: subtitle = "y/n"
        if options == 3: subtitle = "1 / 2"
        if options == 4: subtitle = "1 / 2 / 3 / 4"
        if options == 8: subtitle = "1 / 2 / 3 / 4 / 5 / 6 / 8"
        if options >= 2: subtitle = "1 / 2 ..."
    
    Args:
        title (str, optional): The title to be shown in question Defaults to "Press enter to return main menu".
        options (int, optional): How many options you have. Defaults to 0.
        subtitle (str, optional): Overrides default subtitle which depends on amount of options. Defaults to "↩".
    
    Returns:
        _type_: _description_