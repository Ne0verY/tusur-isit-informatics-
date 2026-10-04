def even_fib_sum(limit):
    # Первые два числа последовательности: F1 = 1, F2 = 2
    a, b = 1, 2
    total_sum = 0
    
    # Пока текущее число (b) не превышает лимит
    while b <= limit:
        # Если число четное, добавляем в сумму
        if b % 2 == 0:
            total_sum += b
        
        # Переходим к следующему числу Фибоначчи, Новое a = старое b, новое b = сумма старых a и b
        a, b = b, a + b
        
    return total_sum
    even_fib_sum(13)        
    even_fib_sum(34)       
    even_fib_sum(100)       
    even_fib_sum(200)    
    even_fib_sum(10000)  
    even_fib_sum(4000000)
