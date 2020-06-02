class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

def findMiddle(head):
    middle = head 
    end = head
    print(head)
    while end.next!= None and end.next.next  != None:
        middle = middle.next
        end = end.next.next
    print(middle.value)

    # print(head.value)
    # print(head.next.value)
    # print(head.next.next.value)
    # print(head.next.next.next.value)
    # print(head.next.next.next.next.value)
    # print(head.next.next.next.next.next.value)
n1 = Node(1)
n1.add(2)
n1.next.add(3)
n1.next.next.add(4)
n1.next.next.next.add(5)
n1.next.next.next.next.add(6)

# reverse(n1)
# print("hello")
findMiddle(n1)























# def reverse(head):
#     before = head
#     worker = head
#     while(worker != None):
#         after = worker.next
#         worker.next = before 
#         before = worker
#         worker = after 
#     head = before 