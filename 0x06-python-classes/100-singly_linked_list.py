#!/usr/bin/python3
"""
This module contains two classe who defines a Node and the other a SinglyLinkedList
"""


class Node:
    """Defines a node"""
    def __init__(self, data, next_node=None):
        """Initialize the data"""
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Getter to access the data value"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter to update the data value
        Raises: TypeError if data is not integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        return self.__data
    
    @property
    def next_node(self):
        """Getter to access the next_node value"""
        return self.__nextnode
    
    @next_node.setter
    def next_node(self, value):
        """Setter to update the next_node value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize the data"""
        self.head = None
    
    def sorted_insert(self, value):
        new = Node(value,
