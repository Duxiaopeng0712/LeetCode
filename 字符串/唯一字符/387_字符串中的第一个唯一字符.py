class Solution:
    def firstUniqChar(s):
        d = {}
        length = len(s)
        for i in range(length):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = length + 1
        ret = min(d.values())
        return -1 if ret > length else ret


if __name__ == '__main__':
    s = "leelcode"
    print(Solution.firstUniqChar(s))

