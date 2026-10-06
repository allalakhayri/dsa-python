

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# -It is the empty string, contains only lowercase characters, or
# -It can be written as AB (A concatenated with B), where A and B are valid strings, or
# -It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        count = 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1

            elif s[i] == ')':
                if count == 0:
                    s[i] = '0'
                else:
                    count -= 1

        count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                count += 1

            elif s[i] == '(':
                if count == 0:
                    s[i] = '0'
                else:
                    count -= 1

        res = ""

        for c in s:
            if c != '0':
                res += c

        return res