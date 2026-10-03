# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ")" and top != '(':
                    return False
                if c == "}" and top != '{':
                    return False
                if c == "]" and top != '[':
                    return False
        if len(stack) != 0:
            return False
        return True


def main():
    s = input().strip()
    sol = Solution()
    print(sol.isValid(s))


if __name__ == "__main__":
    main()
                