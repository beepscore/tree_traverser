#!/usr/bin/env python3

""" tree_traverser contains methods to search a binary tree
"""

def values(nodes):
    """
    :return values of nodes
    """
    # list comprehension returns a generator
    # use list() to convert generator to a list
    vals = (list(node.value for node in nodes))
    return vals

def get_node_with_value(node, value):
    """
    Traverses tree starting at node, depth first
    Note the tree may be a subtree of a larger tree.
    The method may be called recursively.
    :return first node found with value.
    return None if node is None or if not found
    """
    # if node is None:
    #     # edge case
    #     return None

    print("get_node_with_value")
    print("node ", node, "node.value ", node.value)

    if node.children != []:
        for child in node.children:
            # recurse
            got_node = get_node_with_value(child, value)
            if got_node is not None:
                return got_node

    # searched all children, so now consider current node
    if node.value == value:
        # success
        return node
    else:
        return None

