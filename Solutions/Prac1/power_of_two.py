def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
print(is_power_of_two(1))    
print(is_power_of_two(1024))   
print(is_power_of_two(4096))  
print(is_power_of_two(333))
print(is_power_of_two(0))
