# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ')':
                current_depth -= 1
        return max_depth


if __name__ == "__main__":
    s = input("Enter a valid parentheses string: ").strip()
    print(Solution().maxDepth(s))