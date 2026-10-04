from datetime import date

def century_message(name, age, current_year):
    # Вычисляем, через сколько лет человеку исполнится 100
    years_left = 100 - age
    # Прибавляем это количество к текущему году
    target_year = current_year + years_left
    # Возвращаем отформатированное сообщение
    return f"{name}, тебе исполнится 100 лет в {target_year} году"

if __name__ == "__main__":
    # Получаем текущий год автоматически
    current_year = date.today().year
    # Запрашиваем данные у пользователя
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))
    
    # Вызываем функцию и печатаем результат
    print(century_message(user_name, user_age, current_year))