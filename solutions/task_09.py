def max_of_three(a, b, c):
    # Используем встроенную функцию max(), которая принимает любое количество аргументов
    return max(a, b, c)

if __name__ == "__main__":
    # Запрашиваем три числа
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    # Печатаем максимум
    print(max_of_three(a, b, c))