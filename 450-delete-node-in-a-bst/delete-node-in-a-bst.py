# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # if(root.val==key and root.left==None):
        #     return None
        res=root
        def helper(root):
            if(root.left==None):
                return root.right
            elif(root.right==None):
                return root.left
            lastright=find(root.left)
            lastright.right=root.right
            return root.left
        def find(root):
            if root.right==None:
                return root
            else:
                return find(root.right)
        if(root.val==key):
            return helper(root)
        while(root):
            if(root.val>key):
                if(root.left!=None and root.left.val==key):
                    root.left=helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if(root.right!=None and root.right.val==key):
                    root.right=helper(root.right)
                    break
                else:
                    root=root.right
        
        return res
