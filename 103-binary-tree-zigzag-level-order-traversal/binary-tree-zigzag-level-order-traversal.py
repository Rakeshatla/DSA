# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=[root]
        zig=0
        while queue:
            level=len(queue)
            curr=[]
            for _ in range(level):
                node=queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if(zig==0):
                res.append(curr)
                zig=1
            else:
                res.append(curr[::-1])
                zig=0
        return res