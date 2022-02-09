# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, res = [root], []
        while queue:
            for node in queue:
                res.append([node.val])
            res_level = []

            for node in queue:
                if node.left:
                    res_level.append(node.left)
                if node.right:
                    res_level.append(node.right)
            queue = res_level
        return res



        return res

