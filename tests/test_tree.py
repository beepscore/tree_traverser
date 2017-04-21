#!/usr/bin/env python3

import unittest
from tree_traverser import node, tree


class TestTree(unittest.TestCase):

    def test_get_node_with_value(self):
        node0_value = 3
        node0 = node.Node(node0_value)

        actual = tree.get_node_with_value(node0, node0_value)
        self.assertEqual(actual, node0)
