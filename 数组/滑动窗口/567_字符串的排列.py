def checkInclusion(s1, s2):
    # 1、设置要维护的变量
    hashmap1 = {}
    hashmap2 = {}
    for char in s1:
        hashmap1[char] = hashmap1.get(char, 0) + 1
    # 2、设置起始、末尾值
    start = 0
    for end in range(len(s2)):
        hashmap2[s2[end]] = hashmap2.get(s2[end], 0) + 1
        if hashmap1 == hashmap2:
            return True
        # 3、窗口固定：if
        if end >= len(s1) - 1:
            hashmap2[s2[start]] -= 1
            if hashmap2[s2[start]] == 0:
                del hashmap2[s2[start]]
            start += 1
    # 4、返回值
    return False





