#!/usr/bin/env python3

""" binary_tree contains methods to search a binary tree
"""

def is_valid_binary_search_tree(node):
    """
    Traverses tree depth first in order
    """
    return is_valid_bst(node, float('-inf'), float('inf'))


def is_valid_bst(node, value_min, value_max):
    """
    Traverses tree depth first in order
    Note the tree may be a subtree of a larger tree.
    The method may be called recursively.

    Tree does not have to be "balanced", may have more levels than necessary.
    Duplicate values are not allowed.

    https://en.wikipedia.org/wiki/Binary_search_tree
    https://en.wikipedia.org/wiki/Tree_traversal
    http://stackoverflow.com/questions/10832496/finding-if-a-binary-tree-is-a-binary-search-tree?noredirect=1&lq=1
    http://stackoverflow.com/questions/499995/how-do-you-validate-a-binary-search-tree#759851
    http://stackoverflow.com/questions/300935/are-duplicate-keys-allowed-in-the-definition-of-binary-search-trees#300968
    http://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints#7604981
    value_min: initial call should set to float('-inf')
    value_max: initial call should set to float('inf')
    :return True if node is None or is the root of a valid binary search tree
    return False if node value is None or node isn't the root of a valid binary search tree
    return False if tree contains a duplicate value
    """
    print("is_valid_binary_search_tree")

    if node is None:
        # e.g. parent node doesn't have a node at this child
        return True

    if node.value is None:
        return False

    if (node.value > value_min
        and node.value < value_max
        and is_valid_bst(node.left, value_min, node.value)
        and is_valid_bst(node.right, node.value, value_max)):
        return True
    else:
        return False

