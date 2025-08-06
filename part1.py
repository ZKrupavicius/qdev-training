class _Node:
    def __init__(self, data: any, next_ = None) -> None:
        self.data = data
        self.next_ = next_

class List:
    def __init__(self) -> None:
        self._head: "None | _Node" = None
        self._length: int = 0
        
    def __str__(self) -> str:
        result = "["
        current = self._head
        while current is not None:
            result += str(current.data)
            if current.next_ is not None:
                result += ", "
            current = current.next_
        result += "]"
        return result
        
    def append(self, data: any) -> None:
        node = _Node(data)
        self._length += 1
        if self._head is None:
            self._head = node
            return
        current = self._head
        while current.next_ is not None:
            current = current.next_
        current.next_ = node
    
    def __getitem__(self, idx: int):
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        idx = self._make_positive_index(idx)
        current = self._head
        count = 0
        while current is not None:
            if count == idx:
                return current.data
            count +=1
            current = current.next_
        if current is None:
            raise IndexError ("Index out of range.")
    
    def __len__(self) -> int:
        return self._length
        
    def extend(self, items: any) -> None:
        for i in items:
            self.append(i)
            
    def insert(self, idx: int, data: any) -> None:
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        idx = self._make_positive_index(idx)
        node = _Node(data)
        self._length += 1
        if idx == 0:
            node.next_ = self._head
            self._head = node
            return
        current = self._head
        count = 0
        while current is not None and count < idx - 1:
            current = current.next_
            count += 1
        if current is None:
            raise IndexError("List index out of range.")
        node.next_ = current.next_
        current.next_ = node
        
    def __delitem__(self, idx: int) -> None:
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        idx = self._make_positive_index(idx)
        current = self._head
        previous = None
        for i in range(idx):
            previous = current
            current = current.next_
            if current is None:
                raise IndexError("List index out of range.")
        if previous is None:
            self._head = current.next_
        else:
            previous.next_ = current.next_
        self._length -= 1
    
    def remove (self, data: any) -> None:
        current = self._head
        self._length -= 1
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self._head = current.next_
                else:
                    previous.next_ = current.next_
                return
            previous = current
            current = current.next_
        if current is None:
            raise ValueError ("Value not found")
    
    def count(self, data: any) -> int:
        count = 0
        current = self._head
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next_
        return count
    
    def clear(self):
        self._head = None
        
    def pop(self, idx: int = -1) -> None:
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
        idx = self._make_positive_index(idx)
        current = self._head
        self._length -= 1
        previous = None
        for i in range(idx + 1):
            if i == idx:
                if previous is None:
                    self._head = current.next_
                else:
                    previous.next_ = current.next_
                return
            previous = current
            current = current.next_
            if current is None:
                raise IndexError("List index out of range.")
            
    def copy(self) -> any:
        new_list = List()
        current = self._head
        while current is not None:
            new_list.append(current.data)
            current = current.next_
        return new_list
        
    def _make_positive_index(self, idx: int) -> int:
        if idx < 0:
            idx = self._length + idx
        return idx
        
    def index(self, data: any, start: int = 0, end: "int | None" = None) -> int:
        current = self._head
        start = self._make_positive_index(start)
        if end is None:
            end = self._length
        end = self._make_positive_index(end)
        count = 0
        for i in range(start):
            current = current.next_
            count += 1
        for j in range(start, end):
            if current.data == data:
                return count
            current = current.next_
            count += 1
        raise ValueError ("There is no such item.")
        
#    def reverse(self) -> any:
#        current = self._head
#        while current is not None:
        
            

    
if __name__ == "__main__":

    lst = List()
    lst.append(10)
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(lst)
    print(lst[-2])
    lst.extend([40, 60])
    print(lst)
    lst.insert(5, 50)
    print(lst)
    lst.remove(20)
    print(lst)
    print(lst.count(10))
    lst.pop(-1)
    print(lst)
    lst2 = lst.copy()
    lst.clear()
    print(lst)
    print(lst2)
    print(len(lst2))
    lst2.append(10)
    print(lst2)
    print(lst2.index(10, 1, 6))
    print(lst2)
    del lst2[2]
    print(lst2)
    

