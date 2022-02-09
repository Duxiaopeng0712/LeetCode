from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue, depth = [root], 0
        if not root: return 0

        while queue:
            queue_level = []
            for node in queue:
                queue_level.extend([node.left, node.right])
            queue = queue_level
            depth += 1
        return depth-1
