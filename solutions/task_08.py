def century_message(name, age, current_year):
    return f"{name}, тебе исполнится 100 лет в {current_year - age + 100} году"
if __name__ == "__main__":
    print(century_message("Святослав", 20, 2025))
