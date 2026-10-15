# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:pos+1],inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:],inorder[pos+1:])

        return root


def main():
    preorder = list(map(int, input("Enter preorder values separated by spaces: ").split()))
    inorder = list(map(int, input("Enter inorder values separated by spaces: ").split()))

    root = Solution().buildTree(preorder, inorder)
    if root is None:
        print("Built tree: []")
        return

    # Display the tree's values in level order.
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("Built tree (level order):", values)


if __name__ == "__main__":
    main()

        