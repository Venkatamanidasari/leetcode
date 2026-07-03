class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both roots are None, return None to avoid AttributeErrors
        if root1 is None and root2 is None:
            return None
        
        # If one node is None, the merged tree uses the node from the other tree
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        # If both nodes exist, add their values and merge their subtrees recursively
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1
        
