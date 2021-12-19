
# https://leetcode.com/problems/balanced-binary-tree/submissions/

# Time : O(N)

#  Space: O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def helper(node):
        if not node:
            return (True, 0)

        left, right = helper(node.left),helper(node.right)

        balanced=(left[0]and right[0] and abs(left[1]-right[1]) <=1)

        return (balanced,1+max(left[1],right[1]))

    return helper(root)[0]


if __name__ == "__main__":
    # root=TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(20)
    root.right.right = TreeNode(20)



    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(7)

    print(isBalanced(root))
