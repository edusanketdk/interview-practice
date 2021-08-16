def count_zeroes(ar, n):

    # recursive binary seach function
    def first_zero(l, h):
        if h < l:
            return n

        mid = l + (h-l)//2
        if (mid == 0 or ar[mid-1] == 1) and ar[mid] == 0:
            return mid

        if ar[mid] == 0:
            return first_zero(l, mid-1)
        else:
            return first_zero(mid+1, h)

    return n-first_zero(0, n-1)


"""
use binary search to find the index
where first zero occures
then we find the total number of zeroes
by subtracting the index from n

time complexity: O(log(n))
space complexity: O(1)
"""