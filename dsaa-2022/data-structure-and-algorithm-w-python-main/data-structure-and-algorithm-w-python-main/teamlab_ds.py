from typing import Any


class Node():
    """
    A class to represent a Node for an explanation of data structure.
    ...

    Attributes
    ----------
    data : Any
        data that user store on Node instance
    next : Node
        object connected to the next node in a linked list.

    """

    def __init__(self, data : Any = None,  next : 'Node' = None) -> None:
        """
        Args:
            data (Any, optional): data that user store on Node instance
            next (Node, optional): object connected to the next node in a linked list
        """
        self._data = None
        self._next = None

    @property
    def data(self):
        """  data that user store on Node instance """
        return self._data


    @data.setter
    def data(self, value : Any) -> None:
        self._data = value


    @property
    def next(self):
        """ An object connected to the next node in a linked list"""
        return self._next

    @next.setter
    def next(self, node : 'Node') -> None:
        self._next = node

    def __str__(self) -> str:
        return_str = f"I have data : {self._data}\n"
        return_str = return_str + f"I have next node : {self._next}"
        return return_str
