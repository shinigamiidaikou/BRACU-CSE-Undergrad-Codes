class Node:
    def __init__(self, elem, n):
        self.element = elem
        self.next = n


def singlyList(arr):
    nn2 = Node(arr[len(arr)-1], None)
    for i in range(len(arr)-2, -1, -1):
        nn = Node(arr[i], nn2)
        nn2 = nn
    return nn2


def forwardPrint(head):
    if head.next == None:
        print(head.element)
    else:
        print(head.element, end=" --> ")
        n = head.next
        while n.next != None:
            print(n.element, end=" --> ")
            n = n.next
        print(n.element)


def sumOfLastNNodes(head, size, N):
    if N < 0 or N > size:
        return -1
    nn2 = Node(head.element, None)
    n = head.next
    while n != None:
        nn = Node(n.element, nn2)
        nn2 = nn
        n = n.next
    n = nn2  ## new reversed list head node in nn2
    NSum = count = 0
    while count < N:
        NSum = NSum + n.element
        count += 1
        n = n.next
    return NSum


lin = [1, 2, 3, 4, 5, 6, 7]
head1 = singlyList(lin)
forwardPrint(head1)

x = sumOfLastNNodes(head1, 7, 2)

print(f"\nLast N Node Sum: {x}")
