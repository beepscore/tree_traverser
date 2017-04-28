#!/usr/bin/env python3

import unittest
from tree_traverser import node


class TestNode(unittest.TestCase):

    def test_init(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        self.assertIsNotNone(node0)
        self.assertEqual(node0.value, node0_value)
        self.assertEqual(node0.children, [])

        node1_value = 8
        node1 = node.Node(node1_value)
        node0.children.append(node1)
        self.assertEqual(node0.children[0], node1)

    def test_is_leaf_node(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        self.assertTrue(node0.is_leaf_node())

        node1_value = 8
        node1 = node.Node(node1_value)
        node0.children.append(node1)
        self.assertFalse(node0.is_leaf_node())
        self.assertTrue(node1.is_leaf_node())
