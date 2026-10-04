def persistence(num):
    # Если число уже однозначное, шагов 0
    if num < 10:
        return 0
    
    steps = 0
    
    # Пока число состоит из двух и более цифр
    while num >= 10:
        product = 1
        # Перемножаем все цифры числа
        for digit in str(num):
            product *= int(digit)
        
        # Обновляем число и счетчик
        num = product
        steps += 1
        
    return steps
    persistence(39) 
    persistence(999)  
    persistence(25)   
    persistence(4)
