class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        ans = []
        stack = [root]

        while len(stack):
            curr = stack.pop()
            ans.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans