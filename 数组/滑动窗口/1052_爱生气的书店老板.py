def maxSatisfied(customers, grumpy, minutes):
    # 1、定义可维护的变量
    max_satisfied, max_sum, control_start = 0, 0, 0
    # 2、定义窗口首尾端
    start = 0
    for end in range(len(customers)):
        # 3、更新变量
        if grumpy[end] == 1:
            max_sum += customers[end]
        if max_sum > max_satisfied:
            max_satisfied = max_sum
            control_start = start
        # 4、更改窗口大小
        if end >= minutes - 1:
            if grumpy[start]:
                max_sum -= customers[start]
            start += 1
    for i in range(control_start, control_start + minutes):
        grumpy[i] = 0
    # 5、输出结果
    res = 0
    for i in range(len(customers)):
        if not grumpy[i]:
            res += customers[i]

    return res

if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    res = maxSatisfied(customers, grumpy, X)
    print(res)
