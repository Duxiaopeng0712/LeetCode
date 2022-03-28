class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # res = 0
        # for i in range(len(num1) - 1, -1, -1):
        #     for j in range(len(num2) - 1, -1, -1):
        #         res += int(num1[i]) * int(num2[j]) * (10 ** (i+j))
        #
        # return str(res)
        res = 0
        for i, v in enumerate(num1[::-1]):
            for j, u in enumerate(num2[::-1]):
                res += int(v) * int(u) * (10 ** (i + j))
        return str(res)

