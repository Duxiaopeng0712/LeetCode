def longestOnes(nums, k):
    # 1、设置可维护的变量
    max_len, hashmap = 0, {}
    # 2、设置始末值
    start = 0
    for end in range(len(nums)):
        # 3、更新变量
        hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
        if hashmap.get(0, 0) <= k:
            max_len = max(max_len, end - start + 1)
        # 4、窗口不固定，用while
        while hashmap.get(0, 0) > k:
            hashmap[nums[start]] -= 1
            start += 1
    # 5、返回最大值
    return max_len

