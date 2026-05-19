class Solution(object):
    def preorderTraversal(self, root):
        ans = []

        def traversal(curr):
            if not curr:
                return
            ans.append(curr.val)
            traversal(curr.left)
            traversal(curr.right)
            
        traversal(root)
        return ans