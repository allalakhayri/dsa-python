#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary:
        # key   = sorted version of the word (signature)
        # value = list of anagrams
        m = {}

        for word in strs:
            # Create a signature for the word
            # Example: "tea" -> "aet"
            signature = ''.join(sorted(word))

            # If we haven't seen this signature before,
            # create an empty group
            if signature not in m:
                m[signature] = []

            # Add the word to its anagram group
            m[signature].append(word)

        # Return all the groups
        return list(m.values())


def main():
    words = input("Enter words separated by spaces: ").split()
    result = Solution().groupAnagrams(words)
    print(result)


if __name__ == "__main__":
    main()