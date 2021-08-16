def modifytree(head):

    # do preorder traversal
    def preorder(cur):
        if cur is None:
            return
        nodes.append(cur)
        if cur.left:
            preorder(cur.left, nodes)
        if cur.right:
            preorder(cur.right, nodes)

    nodes = []
    preorder(head)

    # create new tree using nodes
    cur = head
    for i in nodes[1:]:
        cur.right = i
        cur = cur.right


"""
instead of modifying the tree, 
we create a new tree 
by traversing the tree in preorder form
and storing the nodes in an array
then traverse the array and 
join every new node to its parent's right
"""



