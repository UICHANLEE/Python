class LinkedListBag():
    def __init__(self, first_node : Node = None) -> None:
        self._head = first_node  
        self._tail = first_node 
        if first_node is not None:
            self._size = 1
        else:
            self._size = 0
        
    def append(self, new_node : Node) -> None:
        if self._size == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

    def insert(self, index_number : int, new_node : Node) -> bool:
        list_index = 0
        cur_node = self._head
        if index_number == 0:
            self._head = new_node
            new_node.next = cur_node
            self._size += 1
            return True

        while cur_node is not None:
            if list_index == index_number:
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            list_index += 1
            pred_node = cur_node 
            cur_node = cur_node.next
        return False

    def remove(self, target_value : int) -> bool:
        cur_node = self._head
        pred_node = cur_node 
        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            pred_node = cur_node 
            cur_node = cur_node.next
        return False        

    def __len__(self):
        return self._size
    
    def __contains__(self, target : int):
        cur_node = self._head
        while cur_node is not None:
            if cur_node.data == target:
                return True
            cur_node = cur_node.next
        return False
    
    def __repr__(self) -> str:
        cur_node = self._head
        if self._size == 0:
            return None

        return_str = ""
        while cur_node is not None:
            return_str += f"{cur_node.data} -> "
            cur_node = cur_node.next
        return_str += f"End of Linked List"
        return return_str

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator():
    def __init__(self, head_node : Node) -> None:
        self._cur_node = head_node
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node
