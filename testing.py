from part1 import List, _Node
import pytest

LIST = List
# LIST = list



def test_node_class():
    node1 = _Node("hello")
    node2 = _Node(2, node1)

    assert node1.data == "hello"
    assert node1.next_ is None
    assert node2.data == 2
    assert node2.next_ == node1
    
def test_append():
    lst = LIST()
    lst.append(10)
    lst.append(20)
    assert str(lst) == "[10, 20]"

def test_list_creation_and_str():
    lst = LIST()
    assert str(lst) == "[]"
    lst.append(1)
    lst.append(2)
    lst.append("hello")
    class MyClass:
        def __repr__(self):
            return "MyClass"
    lst.append(MyClass())
    assert str(lst) == "[1, 2, 'hello', MyClass]"

def test_len():
    lst = LIST()
    assert len(lst) == 0
    lst.append(1)
    lst.append(2)
    assert len(lst) == 2

def test_extend():
    lst = LIST()
    lst.extend([1, 2, 3])
    assert str(lst) == "[1, 2, 3]"

def test_insert():
    lst = LIST()
    lst.extend([1, 3])
    lst.insert(1, 2)
    assert str(lst) == "[1, 2, 3]"
    lst.insert(0, 0)
    assert str(lst) == "[0, 1, 2, 3]"
    lst.insert(100, 6)
    assert str(lst) == "[0, 1, 2, 3, 6]"
    
    with pytest.raises(TypeError):
        lst.insert("a")

def test_getitem():
    lst = LIST()
    lst.extend([1, 2, "hello"])
    assert lst[0] == 1
    assert lst[1] == 2
    assert lst[2] == "hello"
    assert lst[-1] == "hello"

    with pytest.raises(IndexError):
        _ = lst[10]
    with pytest.raises(TypeError):
        _ = lst["1"]

def test_delitem():
    lst = LIST()
    lst.extend([1, 2, 3])
    del lst[1]
    assert str(lst) == "[1, 3]"

    del lst[0]
    assert str(lst) == "[3]"

    with pytest.raises(IndexError):
        del lst[5]
    with pytest.raises(TypeError):
        del lst["a"]

def test_remove():
    lst = LIST()
    lst.extend([1, 2, 3, 2])
    lst.remove(2)
    assert str(lst) == "[1, 3, 2]"

    with pytest.raises(ValueError):
        lst.remove(100)

def test_count():
    lst = LIST()
    lst.extend([1, 2, 2, 3])
    assert lst.count(2) == 2
    assert lst.count(4) == 0
    
def test_clear():
    lst = LIST()
    lst.extend([1, 2, 3])
    lst.clear()
    assert str(lst) == "[]"
    assert len(lst) == 0

def test_pop():
    lst = LIST()
    lst.extend([1, 2, 3])
    lst.pop()
    assert str(lst) == "[1, 2]"
    lst.pop(0)
    assert str(lst) == "[2]"
    
    with pytest.raises(IndexError):
        lst.pop(10)
    with pytest.raises(TypeError):
        lst.pop("a")
        
def test_copy():
    lst1 = LIST()
    lst1.extend([1, 2, 3])
    lst2 = lst1.copy()
    assert str(lst2) == str(lst1)
    lst1.append(4)
    assert str(lst1) != str(lst2)
    
def test_index():
    lst = LIST()
    lst.extend([1, 2, 3, 2, 4])
    assert lst.index(2) == 1
    assert lst.index(2, 2) == 3

    with pytest.raises(ValueError):
        lst.index(10)
        
def test_iter():
    lst = LIST()
    lst.extend([10, 20, 30])
    assert [x for x in lst] == [10, 20, 30]
    
def test_contains():
    lst = LIST()
    lst.extend([1, 2, 3])
    assert (2 in lst)
    assert (3 in lst)
    
def test_setitem():
    lst = LIST()
    lst.extend([10, 20, 30])
    lst[1] = 200
    assert str(lst) == "[10, 200, 30]"
    
    with pytest.raises(IndexError):
        lst[100] = 1

def test_slice():
    lst = LIST()
    lst.extend([10, 20, 30, 40, 50, 60])
    assert str(lst[2:3]) == "[30]"
    assert str(lst[:]) == "[10, 20, 30, 40, 50, 60]"
    assert str(lst[:2]) == "[10, 20]"
    assert str(lst[3:]) == "[40, 50, 60]"
    assert str(lst[::3]) == "[10, 40]"
    assert str(lst[::2]) == "[10, 30, 50]"
    assert str(lst[-2:]) == "[50, 60]"
    assert str(lst[:-1]) == "[10, 20, 30, 40, 50]"