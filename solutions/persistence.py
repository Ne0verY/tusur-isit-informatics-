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

# Проверка
# print(persistence(39))  # 3
# print(persistence(999)) # 4
# print(persistence(4))   # 0

# Поиск числа с устойчивостью 5 (проверка из задания)
# for i in range(1, 1000000):
#     if persistence(i) == 5:
#         print(f"Число с устойчивостью 5: {i}")
#         break
# Ответ для проверки: 679