#!/usr/bin/env python3


class Node:
    """ node for a tree, not necessarily a binary tree.
    For a binary tree, can consider children[0] as "left", children[1] as "right"
    Based on LinkedListNode from hacker_rank_test
    """

    def __init__(self, value):
        """
        :return node with value and children empty list.
        """
        self.value = value
        self.children = []

    def is_leaf_node(self):
        return self.children == []
