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
        actual = tree.get_node_with_value(node0, node0_value, [])
        self.assertEqual(actual, node0)

    def test_get_node_with_value1(self):
        print("test_get_node_with_value1")
        node0_value = 3
        node0 = node.Node(node0_value)

        actual = tree.get_node_with_value(node0, 1, [])
        self.assertEqual(actual, None)

    def test_get_node_with_value_child0(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        child0_value = 2
        child0 = node.Node(child0_value)
        child1_value = 7
        child1 = node.Node(child1_value)
        node0.children = [child0, child1]

        actual = tree.get_node_with_value(node0, 2, [])
        self.assertEqual(actual, child0)

    def test_get_node_with_value_child1(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        child0_value = 2
        child0 = node.Node(child0_value)
        child1_value = 7
        child1 = node.Node(child1_value)
        node0.children = [child0, child1]

        actual = tree.get_node_with_value(node0, 7, [])
        self.assertEqual(actual, child1)
