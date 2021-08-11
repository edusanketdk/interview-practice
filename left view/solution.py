def LeftView(root):
    if root == None:
        return []

    curlvl = 0
    queue = [(root, curlvl)]
    ans = []

    while queue:
        cur, lvl = queue.pop(0)

        if lvl == curlvl:
            ans.append(cur.data)
            curlvl += 1

        if cur.left:
            queue.append((cur.left, lvl+1))
        if cur.right:
            queue.append((cur.right, lvl+1))

    return ans

"""
traverse the tree by level order
using a queue which stores a node and its level

print only that node whose level has not been printed before

time complexity: O(n)
space complexity: O(n)
"""