def reverse_alt_k(head, k):
    cur = start = head
    ar, id = [], 0

    while cur:
        id += 1
        if id%k:
            ar.append(cur.val)
        else:
            ar.append(cur.val)
            print(ar)
            tmpid = 0

            while start and tmpid < k:
                start.val = ar[k-tmpid-1]
                start = start.next
                tmpid += 1

            ar = []
        cur = cur.next

    if id%k:
        print(ar)
        tmpid = 0

        while start and tmpid < k:
            start.val = ar[-tmpid-1]
            start = start.next
            tmpid += 1

        ar = []

"""
traverse the linkedlist
maintain a pointer "start" to every k'th element as we go
store current k elements into an array
traverse the linkedlist from the "start"'th node
store the elements from the array in reverse manner
after we finish the traversal empty the array
"""







