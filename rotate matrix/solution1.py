def rotateby90(a, n):
    for i in range((n+1)//2):
        for j in range(n//2):
            a[i][j], a[n-i-1][n-j-1], a[n-j-1][i], a[j][n-i-1] = \
                a[j][n-i-1], a[n-j-1][i], a[i][j], a[n-i-1][n-j-1]


"""
from the rotation pattern it is observed that 
the rotation of each element can be visualised as a cycle
in which only 4 elements take part at a time

so, 
[i][j]          -> [j][n-i-1]
[n-i-1][n-j-1]  -> [n-j-1][i]
a[n-j-1][i]     -> [i][j]
a[j][n-i-1]     -> [n-i-1][n-j-1]

time complexity: O(n**2)
space complexity: O(1)
"""