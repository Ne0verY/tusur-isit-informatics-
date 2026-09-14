def square_digits(n):
    s = str(n)
    result = ""
    
    for char in s:
        digit = int(char)
        squared = digit ** 2
        result += str(squared)
        
    return int(result)