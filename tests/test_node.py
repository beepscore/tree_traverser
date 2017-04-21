#!/usr/bin/env python3

import unittest
from tree_traverser import node


class TestNode(unittest.TestCase):

    def test_init(self):
        node0_value = 3
        node0 = node.Node(node0_value)
        self.assertIsNotNone(node0)
        self.assertEqual(node0.value, node0_value)
        self.assertEqual(node0.children, [None, None])

        node1_value = 8
        node1 = node.Node(node1_value)
        node0.children[1] = node1
        self.assertEqual(node0.children[1], node1)

