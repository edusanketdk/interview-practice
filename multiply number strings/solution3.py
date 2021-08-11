# for very large numbers
# without directly using multiplication

def multiplyStrings(s1, s2):
    isneg1, isneg2 = 1 if s1[0]=='-' else 0, 1 if s2[0]=='-' else 0
    s1, s2 = s1[1:] if isneg1 else s1, s2[1:] if isneg2 else s2
    finalsign = "-" if isneg1+isneg2 == 1 else ""

    ans = [0]*(len(s1)+len(s2))
    id1, id2 = 0, 0

    for i in s1[::-1]:
        i = ord(i)-48
        id2, carry = 0, 0

        for j in s2[::-1]:
            j = ord(j)-48
            sm = i*j + ans[id1+id2] + carry
            carry = sm//10
            ans[id1+id2] = sm%10
            id2 += 1

        if carry:
            ans[id1+id2] += carry

        id1 += 1

    return finalsign + "".join(map(str, ans[::-1])).lstrip('0')

"""
here we multiply two numbers using school mathematics method

basically multiple second number with each digit of first number
starting in reverse for both numbers
and add the results into an array
"""
