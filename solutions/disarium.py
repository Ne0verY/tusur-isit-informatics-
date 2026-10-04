def is_disarium(n):
    # Преобразуем число в строку для итерации по цифрам
    s = str(n)
    total_sum = 0
    
    # enumerate(s, 1) дает нам индекс (позицию) начиная с 1 и саму цифру
    for i, digit in enumerate(s, 1):
        total_sum += int(digit) ** i
        
    # Сравниваем сумму с исходным числом
    return total_sum == n

# Проверка (можно раскомментировать для теста)
# print(is_disarium(89))   # True
# print(is_disarium(135))  # True
# print(is_disarium(564))  # False