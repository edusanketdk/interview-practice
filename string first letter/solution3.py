import re

def str_fletter(s):
    return "".join(re.findall(r'\b[\w]{1}', s))


"""
find all letters having a boundary before them
and join them into a string
"""