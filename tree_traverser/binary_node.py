#!/usr/bin/env python3


class BinaryNode:
    """ node for a binary tree
    Has 2 children "left" and "right"
    """

    def __init__(self, value):
        """
        :return node with value and children left and right None.
        """
        self.value = value
        self.left = None
        self.right = None

    def is_leaf_node(self):
        return self.left is None and self.right is None
