#!/usr/bin/env python3

import unittest
from tree_traverser import binary_node


class TestBinaryNode(unittest.TestCase):

    def test_init(self):
        node0_value = 3
        node0 = binary_node.BinaryNode(node0_value)
        self.assertIsNotNone(node0)
        self.assertEqual(node0.value, node0_value)
        self.assertIsNone(node0.left)
        self.assertIsNone(node0.right)

        node1_value = 8
        node1 = binary_node.BinaryNode(node1_value)
        node0.left = node1
        self.assertEqual(node0.left, node1)

    def test_is_leaf_node(self):
        node0_value = 3
        node0 = binary_node.BinaryNode(node0_value)

        self.assertIsNotNone(node0)
        self.assertEqual(node0.value, node0_value)
        self.assertIsNone(node0.left)
        self.assertIsNone(node0.right)

        self.assertTrue(node0.is_leaf_node())

        node1_value = 8
        node1 = binary_node.BinaryNode(node1_value)
        node0.left = node1
        self.assertEqual(node0.left, node1)

        self.assertFalse(node0.is_leaf_node())
