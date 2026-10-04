def is_strong(n):
    factorials = {}
    fact = 1
    factorials[0] = 1
    for i in range(1, 10):
        fact *= i
        factorials[i] = fact
    
    total = 0
    for digit in str(n):
        total += factorials[int(digit)]
    
    return total == n

if __name__ == "__main__":
    print(is_strong(1))
    print(is_strong(2))
    print(is_strong(145))
    print(is_strong(123))
    
    strong_numbers = [i for i in range(1, 100001) if is_strong(i)]
    print(strong_numbers)