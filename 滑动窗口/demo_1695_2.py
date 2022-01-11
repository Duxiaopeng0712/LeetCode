def maximumUniqueSubarray(nums):
    # 1、定义要维护的变量
    sums, max_sums, hashmap = 0, 0, {}
    # 2、定义窗口的首尾
    start = 0
    for end in range(len(nums)):
        # 3、更新维护的变量
        # max_sum当且仅当哈希表里面没有重复元素时 (end - start + 1 == len(hashmap)) 更新
        sums += nums[end]
        hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
        if end - start + 1 == len(hashmap):
            max_sums = max(max_sums, sums)
        # 4、维护窗口合法性
        # 根据题意, 题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
        # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
        # 哈希表里面有重复元素时 (end - start + 1 > len(hashmap)) 窗口不合法
        # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap， sum_)
        while end - start + 1 > len(hashmap):
            hashmap[nums[start]] -= 1
            if hashmap[nums[start]] == 0:
                del hashmap[nums[start]]
            sums -= nums[start]
            start += 1
    return max_sums


