def str_fletter(s):
    isspace = True
    for i in s:
        if i == " ":
            isspace = True
        elif isspace:
            print(i, end="")
            isspace = False

"""
print a letter only if its not a space and is preceded by a space
or if it is the first letter of the string
"""