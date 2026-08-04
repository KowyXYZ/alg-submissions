# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        listP = []
        listQ = []

        def calcs(node, param):
            
            if param == 'p':
                if node is None:
                    listP.append(None)
                    return
                listP.append(node.val)
                calcs(node.left, param)
                calcs(node.right, param)

            if param == 'q':
                if node is None:
                    listQ.append(None)
                    return
                listQ.append(node.val)
                calcs(node.left, param)
                calcs(node.right, param)
                   
            # print(param)
            # listP.append(node.val)
            # print(listP)
            

        calcs(p, 'p')
        calcs(q, 'q')

        print(listP)
        print(listQ)

        if listP == listQ:
            return True

        return False