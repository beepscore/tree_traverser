#!/usr/bin/env python3

import unittest
from tree_traverser import node, tree


class TestTree(unittest.TestCase):

    def test_values(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        node1_value = 2
        node1 = node.Node(node1_value)
        node2_value = 7
        node2 = node.Node(node2_value)
        nodes = [node0, node1, node2]
        self.assertEqual(tree.values(nodes), [3, 2, 7])

    def test_get_node_with_value(self):
        print("test_get_node_with_value")
        node0_value = 3
        node0 = node.Node(node0_value)
        actual = tree.get_node_with_value(node0, node0_value)
        self.assertEqual(actual, node0)

    def test_get_node_with_value1(self):
        print("test_get_node_with_value1")
        node0_value = 3
        node0 = node.Node(node0_value)

        actual = tree.get_node_with_value(node0, 1)
        self.assertEqual(actual, None)

    def test_get_node_with_value_child0(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        child0_value = 2
        child0 = node.Node(child0_value)
        child1_value = 7
        child1 = node.Node(child1_value)
        node0.children = [child0, child1]

        actual = tree.get_node_with_value(node0, 2)
        self.assertEqual(actual, child0)

    def test_get_node_with_value_child1(self):
        """
                 3
               /  \
              /    \
             /      \
            2       7
        """
        node0_value = 3
        node0 = node.Node(node0_value)
        child0_value = 2
        child0 = node.Node(child0_value)
        child1_value = 7
        child1 = node.Node(child1_value)
        node0.children = [child0, child1]

        actual = tree.get_node_with_value(node0, 7)
        self.assertEqual(actual, child1)

    def test_get_node_with_value_three_levels_none(self):
        """
                 3
               /  \
              /    \
             /      \
            5       2
           / \     /
          2   3   1
        """
        node0 = node.Node(3)
        node1 = node.Node(5)
        node2 = node.Node(2)
        node3 = node.Node(2)
        node4 = node.Node(3)
        node5 = node.Node(1)

        node0.children = [node1, node2]
        node1.children = [node3, node4]
        node2.children = [node5]

        actual = tree.get_node_with_value(node0, 9)
        self.assertEqual(actual, None)

    def test_get_node_with_value_three_levels(self):
        node0 = node.Node(3)
        node1 = node.Node(5)
        node2 = node.Node(2)
        node3 = node.Node(2)
        node4 = node.Node(3)
        node5 = node.Node(1)

        node0.children = [node1, node2]
        node1.children = [node3, node4]
        node2.children = [node5]

        actual = tree.get_node_with_value(node0, 1)
        self.assertEqual(actual, node5)

    def test_get_node_with_value_three_levels_not_leaf(self):
        """
                 3
               /  \
              /    \
             /      \
            5       2
           / \     /
          2   3   1
        """
        print("test_get_node_with_value_three_levels_not_leaf")

        node0 = node.Node(3)
        node1 = node.Node(5)
        node2 = node.Node(2)
        node3 = node.Node(2)
        node4 = node.Node(3)
        node5 = node.Node(1)

        node0.children = [node1, node2]
        node1.children = [node3, node4]
        node2.children = [node5]

        actual = tree.get_node_with_value(node0, 5)
        self.assertEqual(actual, node1)

    def test_get_node_with_value_three_levels_root(self):
        """
                 3
               /  \
              /    \
             /      \
            5       2
           / \     /
          2   3   1
        """
        print("test_get_node_with_value_three_levels_root")

        node0 = node.Node(7)
        node1 = node.Node(5)
        node2 = node.Node(2)
        node3 = node.Node(6)
        node4 = node.Node(3)
        node5 = node.Node(1)

        node0.children = [node1, node2]
        node1.children = [node3, node4]
        node2.children = [node5]

        actual = tree.get_node_with_value(node0, 7)
        self.assertEqual(actual, node0)
