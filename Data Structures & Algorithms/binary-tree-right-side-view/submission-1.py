# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            depth = len(q)
            for i in range(depth):
                node = q.popleft()

                # if node.left and node.right:
                #     res.append(node.right.val)
                #     q.append(node.left)
                #     q.append(node.right)

                # if node.right is None and node.left:
                #     res.append(node.left)
                #     q.append(node.left)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if i == depth - 1:
                    res.append(node.val)

        
        print(res)

        return res