def tetration(x, n):
    if n == 0:
        return 1
    result = x
    for _ in range(n - 1):
        result = x ** result
    return result

if __name__ == "__main__":
    print(tetration(2, 3))
    print(tetration(3, 2))
    print(tetration(5, 1))
    print(tetration(2, 0))