def fibonacci(n):
    res = []

    a, b = 0, 1
    while n > 0:
        res.append(b)
        a, b = b, a + b
        n -= 1
    return res


if __name__ == '__main__':
    print(fibonacci(10))
