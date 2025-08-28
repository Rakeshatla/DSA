# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftheight(root):
            count=0
            while(root):
                count+=1
                root=root.left
            return count
        def rightheight(root):
            count=0
            while(root):
                count+=1
                root=root.right
            return count
        if not root:
            return 0
        left=leftheight(root)
        right=rightheight(root)
        if(left==right):
            return (1<<left)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        