Intuition:

Preorder traversal follows the order:
Root → Left → Right

So the idea is simple:
Visit the current node first
Then recursively visit the left subtree
Then recursively visit the right subtree

We just need a way to store the visited node values in order.

Approach:

Create an empty array ans to store the result.
Define a helper recursive function traversal(curr):
If the current node is null, return.
Add the current node's value to ans.
Recursively call for the left child.
Recursively call for the right child.
Call this helper function starting from the root.
Return the result array.

Complexity:

Time complexity: O(n)
Each node is visited exactly once.

Space complexity: O(n)
In worst case (skewed tree), recursion stack takes O(n)
Output array also takes O(n)

