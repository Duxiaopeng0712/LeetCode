from typing import List


class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
        temp = ""
        for i in zip(*strs):
            print(i)
            if len(set(i)) == 1:
                temp += i[0]
            else:
                break
        return temp


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(strs))
