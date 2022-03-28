def twoSum(nums, target):
    """
    计算两数的和等于定值，并输出他们所在下标
    :param nums: 数组列表
    :param target: 目标值
    :return:
    """
    # result = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if (nums[i] + nums[j] == target):
    #             result.append(i)
    #             result.append(j)
    #
    #
    # return result
    res = []
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            res.append(i)
            res.append(j)
            break
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return res


if __name__ == '__main__':
    res = twoSum([3, 2, 4], 6)
    print(res)
