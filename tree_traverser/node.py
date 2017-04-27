#!/usr/bin/env python3


class Node:
    """ node for a binary tree.
    Based on LinkedListNode from hacker_rank_test
    """

    def __init__(self, value):
        self.value = value
        # can consider children[0] as "left", children[1] as "right"
        self.children = [None, None]

    def is_leaf_node(self):
        for child in self.children:
            if child is not None:
                return False
        return True

