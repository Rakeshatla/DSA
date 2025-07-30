# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            if(root==None or root==p or root==q):
                return root
            l=dfs(root.left,p,q)
            r=dfs(root.right,p,q)
            if(l==None):
                return r
            elif(r==None):
                return l
            else:
                return root
        return dfs(root,p,q)
        