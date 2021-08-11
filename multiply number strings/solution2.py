# without using int() method

def multiplyStrings(s1, s2):
    isneg1, isneg2 = 1 if s1[0]=='-' else 0, 1 if s2[0]=='-' else 0
    s1, s2 = s1[1:] if isneg1 else s1, s2[1:] if isneg2 else s2
    n1, n2 = 0, 0

    for i in s1:
        n1 *= 10
        n1 += ord(i)-48

    for i in s2:
        n2 *= 10
        n2 += ord(i)-48

    n1, n2 = -n1 if isneg1 else n1, -n2 if isneg2 else n2

    return str(n1*n2)


