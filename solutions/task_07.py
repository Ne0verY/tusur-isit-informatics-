def compare(m, n):
    # Сравниваем числа и возвращаем соответствующую строку
    if m > n:
        return "Number m > n"
    elif m < n:
        return "Number m < n"
    else:
        return "The numbers are equal"

if __name__ == "__main__":
    # Запрашиваем два числа
    m = int(input("Введите число m: "))
    n = int(input("Введите число n: "))
    # Печатаем результат сравнения
    print(compare(m, n))