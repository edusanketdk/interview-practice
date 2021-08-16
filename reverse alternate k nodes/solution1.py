# simplest approach

def reverse_alt_k(head, k):
    ar = []
    cur = head
    while cur:
        ar.append(cur.val)
        cur = cur.next

    br = []
    for i in range(0, len(ar), k):
        cur = ar[i:i+k]
        cur.reverse()

        for j in cur:
            br.append(j)

    newll = linked_list()
    for i in br:
        newll.add_node(i)

    return newll

"""
copy the linkedlist values sequencially to an array
then reverse alternate k elements of the array
create a new linkedlist from the new array
"""