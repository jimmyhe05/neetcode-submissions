from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# sol = Solution()
# print(sol.levelOrder(root))
# print("Expected: [[3], [9, 20], [15, 7]]")

