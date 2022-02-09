class Solution:
    def compressString(S: str) -> str:
        lens = len(S)
        res = ''
        if lens == 0:
            return ""

        start = 0
        end = 0
        while start < lens:
            while end < lens and S[end] == S[start]:
                end += 1
            res += S[start]
            res += str(end - start)
            start = end

        if len(S) < len(res):
            res = S

        return res



if __name__ == '__main__':
    S = "aabcccccaaa"
    # S = "abbccd"
    print(Solution.compressString(S))

