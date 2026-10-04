def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if k > n or n < 0 or k < 0:
        return 0
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    return result

def combinations(n, k):
    if k > n or n < 0 or k < 0:
        return 0
    return arrangements(n, k) // factorial(k)

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(5))
    print(factorial(-1))
    print(arrangements(13, 6))
    print(arrangements(4, 2))
    print(arrangements(5, 5))
    print(arrangements(3, 5))
    print(combinations(13, 6))
    print(combinations(4, 2))
    print(combinations(64, 8))
    print(combinations(5, 0))