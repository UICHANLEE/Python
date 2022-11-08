
from unittest.mock import NonCallableMagicMock
from typing import Any


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, value : Any) -> None:
        self._data = value

    @next.setter
    def next(self, node : Any) -> None:
        self._next = node

    def __str__(self) -> str:
        return_str = f"I have a data: {self._data}\n" \
                    + f"I have a next node : {self._next}"
        return return_str

    def __repr__(self) -> str:
        return_str = f"Node({self._data})"
        return return_str

    def __add__(self, other) -> None:
        self._next = other

class LinkedListBag(object):
    def __init__(self, first_node : Node = None) -> None:
        super().__init__()
        self._head = first_node
        self._tail = first_node

        if first_node is None:
            self._size = 0
        else:
            self._size = self._count()
        
    def __contains__(self, target : int):
        cur_node = self._head
        while cur_node is not None:
            if cur_node.data == target:
                return True
            cur_node = cur_node.next
        else:
            return False
    
    def _count(self) -> int:
        counter = 0
        cur_node = self._head
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        return counter

    def append(self, new_node : Node) -> bool:
        try:
            if self._size == 0:
                self._head = new_node
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, new_node : Node, index_number: int) -> bool:
        index_counter = 0 

        cur_node = self._head

        if index_number == 0:
            new_node.next = self._head
            self._head = new_node
            self._head = new_node
            self._size += 1
            return True # index값이 0일때 추가

        
        while cur_node is not None:
            if index_number == index_counter:
                pass
            pred_node = cur_node
            cur_node = cur_node.next
            index_counter += 1

    def remove(self, target_value : int) -> bool:
        cur_node = self._head

        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next

        return False

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        cur_node = self._head
        if self._size == 0:
            return None

        return_str = ""
        while cur_node is not None:
            return_str += f"{cur_node.data} ->"
            cur_node = cur_node.next
        return_str += f"End of Linked List"
        return return_str

    def __iter__(self):
        return _BagIterator(self._head)

    @property
    def head(self) -> Node:
        return self._head

class _BagIterator():
    def __init__(self, head_node) -> None:
        self._cur_node = head_node
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration

        else:
            node = self._cur_node
            return node
        
    

