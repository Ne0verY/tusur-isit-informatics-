def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
    is_power_of_two(1)    
    is_power_of_two(1024)   
    is_power_of_two(4096)   
    is_power_of_two(333)  
    is_power_of_two(0)
