# Функция перевода метров в сантиметры
def meters_to_centimeters(meters):
    # В 1 метре 100 сантиметров, умножаем на 100
    return meters * 100

if __name__ == "__main__":
    # Запрашиваем у пользователя расстояние в метрах
    # float() используется, чтобы можно было вводить дробные числа (например, 0.5)
    meters = float(input("Введите расстояние в метрах: "))
    # Вызываем функцию и сохраняем результат
    result = meters_to_centimeters(meters)
    # Выводим результат в нужном формате
    print(f"Distance in centimeters: {result}")