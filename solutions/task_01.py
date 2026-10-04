def meters_to_centimeters(meters):
    return meters * 100

if __name__ == "__main__":
    meters = float(input("Введите расстояние в метрах: "))
    result = meters_to_centimeters(meters)
    print(f"Distance in centimeters: {result}")
