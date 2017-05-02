#!/usr/bin/env python3

""" binary_tree contains methods to search a binary tree
"""


def is_valid_binary_search_tree(node, node_values):
    """
    Traverses tree starting at node, depth first
    Note the tree may be a subtree of a larger tree.
    The method may be called recursively.

    Assume tree does not have to be "balanced", may have more levels than necessary.

    Assume duplicate values are not allowed.
    Count all node values, check for duplicates
    node_values is a dictionary of the tree's node values.
    dictionary key is the node value, dictionary value is the count
    if count is > 1, value is duplicated

    http://stackoverflow.com/questions/300935/are-duplicate-keys-allowed-in-the-definition-of-binary-search-trees#300968
    :return True if node is None or is the root of a valid binary search tree
    return False if node value is None or node isn't the root of a valid binary search tree
    return False if tree contains a duplicate value
    """
    print("is_valid_binary_search_tree")

    if node is None:
        # edge case
        return True

    print("node ", node, "node.value ", node.value)

    if node.value is None:
        return False

    if node.value in node_values:
        # duplicate
        node_values[node.value] += 1
        return False
    else:
        node_values[node.value] = 1

    if node.left is not None and node.left.value is not None and node.left.value >= node.value:
        return False

    if node.right is not None and node.right.value is not None and node.right.value <= node.value:
        return False

    # tree is valid so far, check both children
    # recurse
    return is_valid_binary_search_tree(node.left, node_values) and is_valid_binary_search_tree(node.right, node_values)
