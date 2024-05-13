class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.val if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.tail.prev.val if not self.isEmpty() else -1


    def isEmpty(self) -> bool:
         return self.size == 0

    def isFull(self) -> bool:
         return self.size == self.capacity

