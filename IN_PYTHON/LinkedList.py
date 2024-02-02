class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

node1 = node('elem1')

head = node1

node2 = node('elem2')
node3 = node('elem3')
node4 = node('elem4')
node5 = node('elem5')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


#  Insertion of New Node In Beginning

nodeInBeginning = node('new node')
nodeInBeginning.next = head
head = nodeInBeginning


pointer = head

while(pointer!=None):
    print(pointer.value)
    pointer=pointer.next

