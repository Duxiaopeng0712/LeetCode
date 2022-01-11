def lengthOfLongestSubstring(s):
    start = 0
    end = 1
    count = 1
    if len(s) < 2:
        count = len(s)
    while end < len(s):
        if end < len(s) and s[end] not in s[start:end]:
            end += 1
            count = max(count, end - start)
        else:
            start += s[start:end].index(s[end]) + 1
            count = max(count, end - start)
    return count


if __name__ == '__main__':
    s = "nfpdmpi"
    l = lengthOfLongestSubstring(s)
    print(l)
