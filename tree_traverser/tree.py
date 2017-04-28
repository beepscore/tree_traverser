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

def get_node_with_value(node, value, node_stack):
    """
    Traverses tree starting at node, depth first
    Note the tree may be a subtree of a larger tree.
    The method may be called recursively.
    :node_stack is a lifo stack of nodes to visit later
    :return first node found with value.
    return None if node is None or if not found
    """
    # if node is None:
    #     # edge case
    #     return None

    print("get_node_with_value")
    print("node ", node, "node.value ", node.value)
    print("node_stack ", node_stack)

    if node.is_leaf_node():
        if node.value == value:
            # success
            return node
        else:
            # not a match
            if len(node_stack) != 0:
                print("pop")
                node_stack.pop()

    else:
        # not a leaf
        print("append")
        node_stack.append(node)
        print("node_stack ", node_stack)
        print("node_stack values ", values(node_stack))

        for child in node.children:
            # recurse
            print("recurse")
            got_node = get_node_with_value(child, value, node_stack)
            if got_node is not None:
                return got_node

        # searched all children, so now consider current node
        if node.value == value:
            # success
            return node
        else:
            # not a match
            if len(node_stack) != 0:
                print("pop")
                node_stack.pop()

        return None

