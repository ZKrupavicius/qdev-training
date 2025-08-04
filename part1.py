class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class List:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def get(self, idx):
        current = self.head
        count = 0
        while current:
            if count == idx:
                return current
            count +=1
            current = current.next
        
lst = List()
print(lst.head)
lst.append(10)
lst.append(20)
lst.append(30)
print(lst.head.data)
print(lst.get(0).data)
print(lst.get(1).data)
print(lst.get(2).data)