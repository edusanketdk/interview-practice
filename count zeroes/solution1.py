def count_zeroes(ar, n):
    return n-sum(ar)

"""
count of zeroes = total elements - count of ones
since count of ones is equal to sum of list

time complexity: O(n)
space complexity: O(1)
"""