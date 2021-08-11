def rotateby90(a, n):
    # transpose
    for i in range(n):
        for j in range(i, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    # reverse columns
    for i in range(n//2):
        for j in range(n):
            a[i][j], a[n-i-1][j] = a[n-i-1][j], a[i][j]

"""
two simple steps to rotate by 90 anticlockwise
1) transpose the matrix by swapping [i][j] and [j][i]
2) reverse all the columns

time complexity: O(n**2)
space complexity: O(1)
"""