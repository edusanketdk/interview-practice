def intersetPoint(head1, head2):
    # save into lists
    ll1, ll2 = [], []

    tmp = head1
    while tmp:
        ll1.append(tmp.data)
        tmp = tmp.next

    tmp = head2
    while tmp:
        ll2.append(tmp.data)
        tmp = tmp.next

    # reverse the lists
    ll1.reverse()
    ll2.reverse()

    # find where they stop coinciding
    prev = -1
    for i in range(min(len(ll1), len(ll2))):
        if ll1[i] != ll2[i]:
            break
        prev = ll1[i]

    return prev