def square_digits(n):
    s = str(n)
    result = ""
    
    for char in s:
        digit = int(char)
        squared = digit ** 2
        result += str(squared)
        
    return int(result)
    square_digits(3212)  
    square_digits(2112)  
    square_digits(0)      
    square_digits(999) 
    square_digits(10001)
