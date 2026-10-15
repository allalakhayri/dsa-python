# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

class solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def main():
    from collections import deque

    values = input("Enter tree values in level order, separated by spaces (use null for missing nodes): ").split()
    if not values or values[0].lower() == "null":
        print("The tree is empty.")
        return

    root = TreeNode(values[0])
    nodes = deque([root])
    index = 1
    while nodes and index < len(values):
        current = nodes.popleft()
        for side in ("left", "right"):
            if index >= len(values):
                break
            value = values[index]
            index += 1
            if value.lower() != "null":
                child = TreeNode(value)
                setattr(current, side, child)
                nodes.append(child)

    p_value = input("Enter the value of node p: ")
    q_value = input("Enter the value of node q: ")

    def find_node(node, value):
        if node is None:
            return None
        if node.val == value:
            return node
        return find_node(node.left, value) or find_node(node.right, value)

    p = find_node(root, p_value)
    q = find_node(root, q_value)
    if p is None or q is None:
        print("One or both values were not found in the tree.")
        return

    ancestor = solution().lowestCommonAncestor(root, p, q)
    print("Lowest common ancestor:", ancestor.val)


if __name__ == "__main__":
    main()