#!/usr/bin/env python3

import unittest
from tree_traverser import node, tree


class TestTree(unittest.TestCase):

    def test_init(self):
        node0_value = 3
        node0 = node.Node(node0_value)

        oak_tree = tree.Tree(node0)
        self.assertEqual(oak_tree.root, node0)
