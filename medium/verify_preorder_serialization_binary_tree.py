# One way to serialize a binary tree is to use preorder traversal.
# When we encounter a non-null node, we record the node's value. 
# If it is a null node, we record using a sentinel value such as '#'.




class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        diez = 1

        for node in preorder.split(','):
            diez -=1

            if diez < 0 :
                return False 
            if node != '#':
                diez += 2
        return diez == 0


if __name__ == "__main__":
    preorder = input("Enter preorder serialization: ")
    print(Solution().isValidSerialization(preorder))
        