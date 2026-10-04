def sum_interval(a, b):
    if a > b:
        a, b = b, a
        
    n = b - a + 1
    return n * (a + b) // 2
    sum_interval(1, 0)   
    sum_interval(1, 2)  
    sum_interval(-1, 2)   
    sum_interval(5, 5)
