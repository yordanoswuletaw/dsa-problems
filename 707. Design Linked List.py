class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        # if index out of range
        if self.count <= index or index < 0:
            return -1
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val  

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        self.count += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new
        else:
            self.head = new
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        elif 0 < index < self.count:
            new = Node(val)
            curr = self.head
            while index > 1:
                curr = curr.next
                index -= 1
            new.next = curr.next
            curr.next = new
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        # if index out of bound
        if self.count <= index or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            while index > 1:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next
        self.count -= 1
        
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
