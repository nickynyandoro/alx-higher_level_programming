#!/usr/bin/python3
if_name_=="_main_":
    """Print all names defined by_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "_":
            print(name)
