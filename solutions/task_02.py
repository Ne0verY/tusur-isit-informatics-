def bytes_to_kilobytes(value):
    return value / 1024

def kilobytes_to_bytes(value):
    return value * 1024

if __name__ == "__main__":
    number = float(input("Введите число: "))
    direction = input("Введите направление перевода (b_to_kb или kb_to_b): ").strip().lower()
    
    if direction == "b_to_kb":
        print(bytes_to_kilobytes(number))
    elif direction == "kb_to_b":
        print(kilobytes_to_bytes(number))
    else:
        print("Неверное направление перевода.")
