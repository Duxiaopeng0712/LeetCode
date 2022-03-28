def maximumUniqueSubarray(nums):
    sums = 0
    max_sums = 0
    array_Set = set()

    for end in range(len(nums)):
        while array_Set and nums[end] in array_Set:
            array_Set.remove(nums[end])
            sums -= nums[end]
        array_Set.add(nums[end])
        sums += nums[end]
        max_sums = max(max_sums, sums)

    return max_sums

if __name__ == '__main__':
    # nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    # nums = [558,508,782,32,187,103,370,607,619,267,984,10]
    nums = [4,2,4,5,6]
    # nums =[187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
    l = maximumUniqueSubarray(nums)
    print(l)
