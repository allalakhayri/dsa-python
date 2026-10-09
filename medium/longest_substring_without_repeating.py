# Given a string s, find the length of the longest substring without duplicate characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        st = set()
        res = 0

        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1

            st.add(s[right])
            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    s = input("Enter a string: ")
    solution = Solution()
    print(f"Input: {s!r} -> {solution.lengthOfLongestSubstring(s)}")
