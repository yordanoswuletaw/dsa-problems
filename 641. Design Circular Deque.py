class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.size = 0
        self.maxSize = k
        

    def insertFront(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False

        new_node = Node(value)
        if self.front:
            new_node.next = self.front
            new_node.prev = self.rear
            self.front.prev = new_node
            self.rear.next = new_node
            self.front = new_node
        else:
            self.front = self.rear = new_node
        self.size += 1

        return True    

    def insertLast(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False

        new_node = Node(value)
        if self.rear:
            new_node.next = self.front
            new_node.prev = self.rear
            self.front.prev = new_node
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.front:
            if self.front is self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = self.rear
                self.rear.next = self.front
            self.size -= 1
            return True

        return False

    def deleteLast(self) -> bool:
        if self.rear:
            if self.front is self.rear:
                self.front = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = self.front
                self.front.prev = self.rear
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.front:
            return self.front.val
        return -1

    def getRear(self) -> int:
        if self.rear:
            return self.rear.val
        return -1
        
    def isEmpty(self) -> bool:
        return self.size == 0 or not self.front

    def isFull(self) -> bool:
        return self.size == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
