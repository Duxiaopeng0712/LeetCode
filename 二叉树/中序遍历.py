# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        stack, res = [root], []

        while stack:
            temp = stack.pop()
            if isinstance(temp, TreeNode):
                stack.extend([temp.right, temp.val, temp.left])
            elif isinstance(temp, int):
                res.append(temp)
        return res


