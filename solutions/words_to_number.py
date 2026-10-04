def words_to_number(text):
    # Словарь чисел
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    scales = {
        "thousand": 1000,
        "million": 1000000
    }

    # Разбиваем строку на слова, игнорируя "and" и дефисы
    # Заменяем дефисы на пробелы, чтобы "twenty-one" стало "twenty one"
    words = text.replace('-', ' ').split()
    
    result = 0
    current = 0
    
    for word in words:
        if word == "and":
            continue
            
        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in scales:
            # Умножаем накопленное на коэффициент (1000 или 1 млн)
            result += current * scales[word]
            current = 0
            
    return result + current

print(words_to_number("one"))       
print(words_to_number("twenty"))        
print(words_to_number("two hundred forty-six"))  
print(words_to_number("seven hundred eighty-three thousand nine hundred and nineteen"))
