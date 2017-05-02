#!/usr/bin/env python3

import unittest
from tree_traverser import binary_node, binary_tree


class TestTree(unittest.TestCase):

    def test_is_valid_binary_search_tree_none(self):
        self.assertTrue(binary_tree.is_valid_binary_search_tree(None, {}))

    def test_is_valid_binary_search_tree_one_level_true(self):
        """
                 -5
        """
        node0 = binary_node.BinaryNode(-5)
        # explicitly set left, don't explicilty set right
        node0.left = None

        self.assertIsNone(node0.left)
        self.assertIsNone(node0.right)
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0, {}))

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

        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0, {}))

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

        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0, {}))

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
        self.assertTrue(binary_tree.is_valid_binary_search_tree(node0, {}))

        # add repeated value to make tree invalid
        node0.right.left = binary_node.BinaryNode(2)
        self.assertFalse(binary_tree.is_valid_binary_search_tree(node0, {}))

    # def test_is_valid_binary_search_tree_three_levels_none(self):
    #     """
    #              3
    #            /  \
    #           /    \
    #          /      \
    #         5       2
    #        / \     /
    #       2   3   1
    #     """
    #     node0 = node.Node(3)
    #     node1 = node.Node(5)
    #     node2 = node.Node(2)
    #     node3 = node.Node(2)
    #     node4 = node.Node(3)
    #     node5 = node.Node(1)
    #
    #     node0.children = [node1, node2]
    #     node1.children = [node3, node4]
    #     node2.children = [node5]
    #
    #     actual = tree.get_node_with_value(node0, 9)
    #     self.assertEqual(actual, None)
    #
    # def test_get_node_with_value_three_levels(self):
    #     node0 = node.Node(3)
    #     node1 = node.Node(5)
    #     node2 = node.Node(2)
    #     node3 = node.Node(2)
    #     node4 = node.Node(3)
    #     node5 = node.Node(1)
    #
    #     node0.children = [node1, node2]
    #     node1.children = [node3, node4]
    #     node2.children = [node5]
    #
    #     actual = tree.get_node_with_value(node0, 1)
    #     self.assertEqual(actual, node5)
    #
    # def test_get_node_with_value_three_levels_not_leaf(self):
    #     """
    #              3
    #            /  \
    #           /    \
    #          /      \
    #         5       2
    #        / \     /
    #       2   3   1
    #     """
    #     node0 = node.Node(3)
    #     node1 = node.Node(5)
    #     node2 = node.Node(2)
    #     node3 = node.Node(2)
    #     node4 = node.Node(3)
    #     node5 = node.Node(1)
    #
    #     node0.children = [node1, node2]
    #     node1.children = [node3, node4]
    #     node2.children = [node5]
    #
    #     actual = tree.get_node_with_value(node0, 5)
    #     self.assertEqual(actual, node1)
    #
    # def test_get_node_with_value_three_levels_root(self):
    #     """
    #              7
    #            /  \
    #           /    \
    #          /      \
    #         5       2
    #        / \     /
    #       6   3   1
    #     """
    #     node0 = node.Node(7)
    #     node1 = node.Node(5)
    #     node2 = node.Node(2)
    #     node3 = node.Node(6)
    #     node4 = node.Node(3)
    #     node5 = node.Node(1)
    #
    #     node0.children = [node1, node2]
    #     node1.children = [node3, node4]
    #     node2.children = [node5]
    #
    #     actual = tree.get_node_with_value(node0, 7)
    #     self.assertEqual(actual, node0)
    #
    # def test_get_node_with_value_non_binary_four_levels(self):
    #     """
    #     non-binary tree
    #
    #              7
    #            /  \
    #           /    \
    #          /      \
    #         5       2
    #        / \     /
    #       6   3   1
    #          /| \
    #         / |  \
    #        8  9   1
    #     """
    #     node0 = node.Node(7)
    #     node1 = node.Node(5)
    #     node2 = node.Node(2)
    #     node3 = node.Node(6)
    #     node4 = node.Node(3)
    #     node5 = node.Node(1)
    #     node6 = node.Node(8)
    #     node7 = node.Node(9)
    #     node8 = node.Node(1)
    #
    #     node0.children = [node1, node2]
    #     node1.children = [node3, node4]
    #     node2.children = [node5]
    #     node4.children = [node6, node7, node8]
    #
    #     self.assertEqual(tree.get_node_with_value(node0, 7), node0)
    #     self.assertEqual(tree.get_node_with_value(node0, 5), node1)
    #     self.assertEqual(tree.get_node_with_value(node0, 2), node2)
    #     self.assertEqual(tree.get_node_with_value(node0, 6), node3)
    #     self.assertEqual(tree.get_node_with_value(node0, 3), node4)
    #     self.assertEqual(tree.get_node_with_value(node0, 3), node4)
    #     self.assertEqual(tree.get_node_with_value(node0, 9), node7)
    #     self.assertEqual(tree.get_node_with_value(node0, 1), node8)
