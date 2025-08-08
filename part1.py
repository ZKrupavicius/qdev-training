from typing import Union

class _Node:
    def __init__(self, data: any, next_: "_Node | None" = None) -> None:
        self.data = data
        self.next_ = next_

class List:
    def __init__(self) -> None:
        self._head: None | _Node = None
        self._length: int = 0
        
    def __str__(self):
        return repr(self)
    
    def __repr__(self):
        return "[" + ", ".join(repr(data) for data in self) + "]"
    
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
    
    def __getitem__(self, idx: Union[int, slice]) -> any:       
        if isinstance(idx, slice):
            if idx.start is None:
                _start = 0
            else:
                _start = idx.start
                _start = self._make_positive_index(_start)
            if idx.stop is None:
                _stop = self._length
            else:
                _stop = idx.stop
                _stop = self._make_positive_index(_stop)
            if idx.step is None:
                _step = 1
            else:
                _step = idx.step
                
            current = self._head 
            new_list = self.__class__()
            for i in range(_start):
                current = current.next_
            for j in range(_start,  _stop):
                new_list.append(current.data)
                for i in range(_step):
                    if current.next_ is not None:
                        current = current.next_
                    else:
                        return new_list
                if current is None:
                    return new_list 
                j += _step
            return new_list   
            
        else:
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
            
        if idx > self._length:
            idx = self._length
            
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
    
    def remove(self, data: any) -> None:
        previous = None
        
        for node in self._node_iter():
            if node.data == data:
                self._length -= 1
                if previous is None:
                    self._head = node.next_
                else:
                    previous.next_ = node.next_
                return
            previous = node
        raise ValueError("Value not found")
    
    def count(self, data: any) -> int:
        count = 0
        current = self._head
        
        while current is not None:
            if current.data == data:
                count += 1
            current = current.next_
        return count
    
    def clear(self) -> None:
        self._head = None
        self._length = 0
        
    def pop(self, idx: int = -1) -> any:
        if not isinstance (idx, int):
            raise TypeError ("Given index should be an integer.")
            
        if self._length == 0:
            raise IndexError("Cannot do that from empty list")
            
        idx = self._make_positive_index(idx)
        current = self._head
        previous = None
        
        for i in range(idx + 1):
            if i == idx:
                self._length -= 1
                removed = current.data
                if previous is None:
                    self._head = current.next_
                else:
                    previous.next_ = current.next_
                return removed
            previous = current
            current = current.next_
            if current is None:
                raise IndexError("List index out of range.")
            
    def copy(self) -> any:
        return self[:]
        
    def _make_positive_index(self, idx: int) -> int:
        if idx < 0:
            idx = self._length + idx
            
        if idx < 0 or idx > self._length:
            raise IndexError("Index out of range.")
        return idx
        
    def index(self, data: any, start: int = 0, end: Union[int, None] = None) -> int:
        current = self._head
        start = self._make_positive_index(start)
        
        if end is None:
            end = self._length
        else:
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
    
    def __iter__(self):
        for node in self._node_iter():
            yield node.data
        
    def _node_iter(self) -> None:
        current = self._head
        
        while current is not None:
            yield current
            current = current.next_
            
    def __contains__(self, data: any) -> bool:
        return any(node.data == data for node in self._node_iter())
        
    def __setitem__(self, idx: int, data: any) -> None:
        if not isinstance(idx, int):
            raise TypeError("Given index should be an integer.")
            
        idx = self._make_positive_index(idx)
        current = self._head
        count = 0
        
        while current is not None:
            if count == idx:
                current.data = data
                return
            current = current.next_
            count += 1
        raise IndexError("Index out of range.")
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, List):
            return False
        return list(self) == list(other)
            