# Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2.
# subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.



class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lengths = {0: 0}
        longest = 0

        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")

            if "." in name:
                longest = max(
                    longest,
                    lengths[depth] + len(name)
                )
            else:
                lengths[depth + 1] = (
                    lengths[depth] + len(name) + 1
                )

        return longest


def main():
    solution = Solution()
    test_cases = [
        "dir\n\tsubdir\n\t\tfile.txt",
        "dir\n\tsubdir\n\t\tfile.txt\n\t\tsubdir2\n\t\t\tfile2.txt",
    ]

    for case in test_cases:
        print(solution.lengthLongestPath(case))


if __name__ == "__main__":
    main()