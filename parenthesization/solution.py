def parenthesization(head: Node, s: list):
    if head is None:
        return

    s.append(str(head.data))

    if not (head.left or head.right):
        return

    s.append('(')
    parenthesization(head.left, s)
    s.append(')')

    if head.right:
        s.append('(')
        parenthesization(head.right, s)
        s.append(')')


"""
This method is used to store graphs in memory 
if a node doesn't have children, no brackets needed
bracket for left child is compulsory
bracket for right child is not needed if there is no right child

Time complexity: O(n)
Space complexity: O(n)
"""


