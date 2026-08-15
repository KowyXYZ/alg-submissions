# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # if not preorder:
        #      return None
        
      
        # root = preorder[0]

        # i = inorder.index(root)
        # l = inorder[:i]
        # r = inorder[i + 1:]
     
        # res = TreeNode(root)

                
        
        # #print('LEFT AND RIGHT', l, r)

        # l_preorder = preorder[1:1 + len(l)]
        # r_preorder = preorder[1 + len(l):]

        # res.left = self.buildTree(l_preorder, l)
        # res.right = self.buildTree(r_preorder, r)

        # return res

        p = 0
        i = 0

        def build(stop=None):
            nonlocal p, i

            if p == len(preorder):
                return None

            if stop is not None and inorder[i] == stop:
                i += 1
                return None

            root = preorder[p]
            p += 1

            res = TreeNode(root)

            res.left = build(root)
            res.right = build(stop)

            return res

        return build()