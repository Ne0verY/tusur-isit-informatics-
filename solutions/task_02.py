# Функция перевода байтов в килобайты
def bytes_to_kilobytes(value):
    # В 1 килобайте 1024 байта, делим на 1024
    return value / 1024

# Функция перевода килобайтов в байты
def kilobytes_to_bytes(value):
    # Умножаем на 1024
    return value * 1024

if __name__ == "__main__":
    # Спрашиваем у пользователя число
    number = float(input("Введите число: "))
    # Спрашиваем направление перевода
    direction = input("Введите направление перевода (b_to_kb или kb_to_b): ").strip().lower()
    
    if direction == "b_to_kb":
        # Если переводим из байтов в килобайты
        print(bytes_to_kilobytes(number))
    elif direction == "kb_to_b":
        # Если переводим из килобайтов в байты
        print(kilobytes_to_bytes(number))
    else:
        print("Неверное направление перевода.")