def addTwoLists(first, second):
    n1, n2 = 0, 0
    while first:
        n1 = n1*10 + first.data
        first = first.next
    while second:
        n2 = n2*10 + second.data
        second = second.next

    n_ans = str(n1+n2)
    ll_ans = LinkedList()
    for i in n_ans:
        ll_ans.insert(int(i))

    return ll_ans.head

"""
Extract the numbers from the two linkedlists
add those and store into a string
create a new linkedlist and 
add the digits into the newly created linkedlist

Note: this approach requires us to be able to
create a new linkedlist. 

Time complexity: O(N+M)
space complexity: O(max(N, M))
"""