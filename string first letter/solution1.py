def str_fletter(s):
    return "".join(map(lambda x: x[0], s.split()))

"""
split the string into a list with space as separator
create a new list with only first letter of a string in the original list
join the list into a string
"""