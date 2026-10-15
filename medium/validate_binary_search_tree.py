# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    values = input("Enter tree values in level order (use null for missing nodes): ").split()

    if not values or values[0].lower() == "null":
        root = None
    else:
        root = TreeNode(int(values[0]))
        queue = [root]
        index = 1
        parent_index = 0

        while parent_index < len(queue) and index < len(values):
            parent = queue[parent_index]
            parent_index += 1

            if values[index].lower() != "null":
                parent.left = TreeNode(int(values[index]))
                queue.append(parent.left)
            index += 1

            if index < len(values):
                if values[index].lower() != "null":
                    parent.right = TreeNode(int(values[index]))
                    queue.append(parent.right)
                index += 1

    print(Solution().isValidBST(root))
