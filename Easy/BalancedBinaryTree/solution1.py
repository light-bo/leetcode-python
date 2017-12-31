# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in
# which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if self.isBalanced(root.left):
            left_depth = self.treeDepth(root.left)
        else:
            return False

        if self.isBalanced(root.right):
            right_depth = self.treeDepth(root.right)
        else:
            return False


        interval = abs(left_depth - right_depth)

        return True if interval <= 1 else False


    def treeDepth(self, tree):
        if tree is None:
            return 0

        if tree.left is None and tree.right is None:
            return 1

        return max(self.treeDepth(tree.left), self.treeDepth(tree.right)) + 1
