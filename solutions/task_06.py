def echo_number(number):
    # Возвращаем строку в точном соответствии с примером
    return f"That's the number you entered {number}"

if __name__ == "__main__":
    # Запрашиваем число
    num = input("Введите число: ")
    # Печатаем результат
    print(echo_number(num))