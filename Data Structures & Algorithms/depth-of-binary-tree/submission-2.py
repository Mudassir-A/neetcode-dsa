# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursiveDFS(root):
            if not root:
                return 0

            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

            return 1 + max(leftDepth, rightDepth)

        def iterativeDFS(root):
            stack = [[root, 1]]
            maxDepth = 0

            while stack:
                node, depth = stack.pop()

                if node:
                    maxDepth = max(maxDepth, depth)
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])

            return maxDepth

        def BFS(root):
            q = deque()
            if root:
                q.append(root)

            level = 0
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1

            return level

        # return recursiveDFS(root)
        # return iterativeDFS(root)
        return BFS(root)
