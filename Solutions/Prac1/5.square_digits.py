def square_digits(n):
    s = str(n)
    result = ""
    
    for char in s:
        digit = int(char)
        squared = digit ** 2
        result += str(squared)
        
    return int(result)
print(square_digits(3212))  
print(square_digits(2112)) 
print(square_digits(0)) 
print(square_digits(999))
print(square_digits(10001))
