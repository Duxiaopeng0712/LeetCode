arr = [-8, 2, 0, 9, 1, -4, 2, 18]
arr.sort()
k = 10
temp = []
i = 0
j = len(arr) - 1

while i < j:
    if arr[i] + arr[j] == k:
        temp.append(arr[i])
        temp.append(arr[j])
        i += 1
        j -= 1
    elif arr[i] + arr[j] > k:
        j -= 1
    else:
        i += 1

print(temp)


