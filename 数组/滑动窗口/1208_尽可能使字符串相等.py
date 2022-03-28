def equalSubString(s, t, maxCost):
    # 1、定义要维护的变量
    total_cost, max_len = 0, 0
    # 2、定义首尾值
    start = 0
    for end in range(len(t)):
        # 3、维护变量
        total_cost += abs(ord(s[end]) - ord(t[end]))
        if total_cost <= maxCost:
            max_len = max(max_len, end - start + 1)
        # 4、窗口固定，用while
        while total_cost > maxCost:
            total_cost -= abs(ord(s[start]) - ord(t[start]))
            start += 1
    # 5、返回最终值
    return max_len
