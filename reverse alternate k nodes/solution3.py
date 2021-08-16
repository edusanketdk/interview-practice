# reverse a linked list without extra space

def reverse(head, k):
    if head == None:
        return None

    current = head
    nxt = prev = None
    count = 0

    while(current is not None and count < k):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        count += 1

    if nxt is not None:
        head.next = self.reverse(nxt, k)

    return prev


"""
basically we change the direction of pointers here
store cur -> next into a variable
make cur -> next = cur's previous node
make prev = cur
make cur = next (which was stored earlier)

finally point the head to the prev
"""