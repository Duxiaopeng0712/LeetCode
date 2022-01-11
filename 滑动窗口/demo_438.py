def findAnagrams(s, p):
    # 1、定义要维护的变量
    res, hashmap, temp_map = [], {}, {}
    if len(s) < len(p):
        return res
    for char in p:
        temp_map[char] = temp_map.get(char, 0) + 1
    # 2、定义起始变量
    start = 0
    for end in range(len(s)):
        # 3、更新要维护的变量
        hashmap[s[end]] = hashmap.get(s[end], 0) + 1
        if hashmap == temp_map:
            res.append(start)
        if end >= len(p) - 1:
            hashmap[s[start]] -= 1
            if(hashmap[s[start]] == 0):
                del hashmap[s[start]]
            start += 1
    print(res)
    # 5、输出结果
    return res
if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"

    findAnagrams(s, p)
