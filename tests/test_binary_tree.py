#!/usr/bin/env python3

import unittest
from tree_traverser import binary_node, binary_tree


class TestTree(unittest.TestCase):

    def test_is_valid_binary_search_tree_none(self):
        self.assertTrue(binary_tree.is_valid_binary_search_tree(None))

    def test_is_valid_binary_search_tree_one_level_true(self):
        """
                 -5
        """
        node0 = binary_node.BinaryNode(-5)
        # explicitly set left, don't explicitly set right
        node0.left = None

        self.assertIsNone(node0.left)
        self.assertIsNone(node0.right)
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_two_levels_true(self):
        """
                 3
               /  \
              /    \
             /      \
            2       7
        """
        node0 = binary_node.BinaryNode(3)
        node0.left = binary_node.BinaryNode(2)
        node0.right = binary_node.BinaryNode(7)

        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_two_levels_false(self):
        """
                 3
               /  \
              /    \
             /      \
            2       1
        """
        node0 = binary_node.BinaryNode(3)
        node0.left = binary_node.BinaryNode(2)
        node0.right = binary_node.BinaryNode(1)

        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_repeated(self):
        """
                 3
               /  \
              /    \
             /      \
            2       7
                   /
                  2
        """
        node0 = binary_node.BinaryNode(3)
        node0.left = binary_node.BinaryNode(2)
        node0.right = binary_node.BinaryNode(7)

        # no repeated values
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0))

        # add repeated value to make tree invalid
        node0.right.left = binary_node.BinaryNode(2)
        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_three_levels_false(self):
        """
        In a valid sort tree, depth first in order traversal produces a sorted list.
        This tree is not a valid binary search tree.
        https://en.wikipedia.org/wiki/Binary_search_tree

                20
               /  \
              /    \
             /      \
           10        30
                    /  \
                   5    40
        """
        node0 = binary_node.BinaryNode(20)
        node1 = binary_node.BinaryNode(10)
        node2 = binary_node.BinaryNode(30)
        node3 = binary_node.BinaryNode(5)
        node4 = binary_node.BinaryNode(40)

        node0.left = node1
        node0.right = node2

        node2.left = node3
        node2.right = node4

        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_three_levels_child_none(self):
        """
                 5
               /  \
              /    \
             /      \
            3       7
           / \     /
          2   4   6
        """
        node0 = binary_node.BinaryNode(5)
        node1 = binary_node.BinaryNode(3)
        node2 = binary_node.BinaryNode(7)
        node3 = binary_node.BinaryNode(2)
        node4 = binary_node.BinaryNode(4)
        node5 = binary_node.BinaryNode(6)

        node0.left = node1
        node0.right = node2

        node1.left = node3
        node1.right = node4

        node2.left = node5

        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0))

    def test_is_valid_binary_search_tree_four_levels(self):
        """
                 5
               /  \
              /    \
             /      \
            4        7
           / \      /
          2   9    6
             / \
            8   11
        """
        node0 = binary_node.BinaryNode(5)
        node1 = binary_node.BinaryNode(4)
        node2 = binary_node.BinaryNode(7)
        node3 = binary_node.BinaryNode(2)
        node4 = binary_node.BinaryNode(9)
        node5 = binary_node.BinaryNode(6)
        node6 = binary_node.BinaryNode(8)
        node7 = binary_node.BinaryNode(11)

        node0.left = node1
        node0.right = node2

        node1.left = node3
        node1.right = node4

        node2.left = node5

        node4.left = node6
        node4.right = node7

        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0))

        # manually check subtrees
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node1))
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node2))

        self.assertTrue(binary_tree.is_valid_binary_search_tree(node3))
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node4))

