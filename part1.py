class Node:
    def __init__(self, data: any, next = None):
        self.data = data
        self.next = next
        
    def __str__(self):
        str = f'{self.data}'
        if self.next is not None:
            str += f', {self.next}'
        return str

class List:
    def __init__(self):
        self.head: "None | Node" = None
        
    def __str__(self):
        if self.head is None:
            return "[]"
        return "[" + str(self.head) + "]"
        
    def append(self, data: any):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    
    def __getitem__(self, idx: int):
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        current = self.head
        count = 0
        while current is not None:
            if count == idx:
                return current.data
            count +=1
            current = current.next
        if current is None:
            raise IndexError ("Index out of range.")
    
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        
    def extend(self, items):
        for i in items:
            self.append(i)
            
    def insert(self, idx: int, data: any):
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        node = Node(data)
        if idx == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        count = 0
        while current is not None and count < idx - 1:
            current = current.next
            count += 1
        if current is None:
            raise IndexError("List index out of range.")
        node.next = current.next
        current.next = node
    
    def remove (self, data: any):
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        if current is None:
            raise ValueError ("Value not found")
    
    def count(self, data: any):
        count = 0
        current = self.head
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next
        return count
    
    def clear(self):
        self.head = None
        
    def pop(self, idx: int = -1):
        current = self.head
        previous = None
        if idx == -1:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = current.next
            return
        for i in range(idx + 1):
            if i == idx:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
            if current is None:
                raise IndexError("List index out of range.")
            
            
        
#    def index(idx: int, start: int, end: int)
    
    

lst = List()
lst.append(10)
lst.append(10)
lst.append(20)
lst.append(30)
lst.extend([40, 60])
lst.insert(5, 50)
lst.remove(20)
print(lst)
print(lst.count(10))
lst.pop(1)
print(lst)
lst.clear()
print(lst)

