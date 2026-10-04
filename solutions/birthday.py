import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    
    prob_no_match = 1.0
    for i in range(people):
        prob_no_match *= (365 - i) / 365
        
    return 1.0 - prob_no_match

def simulate_birthday(people, trials):
    matches_count = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(set(birthdays)) < people:
            matches_count += 1
    return matches_count / trials

if __name__ == "__main__":
    print("--- Точный расчет ---")
    print(f"1 человек: {birthday_probability(1)}")
    print(f"23 человека: {birthday_probability(23)}")
    print(f"50 человек: {birthday_probability(50)}")
    print(f"366 человек: {birthday_probability(366)}")

    print("\n--- Симуляция ---")
    print(f"23 человека (100000 испытаний): {simulate_birthday(23, 100000)}")

    print("\n--- Таблица ---")
    print(f"{'Люди':<6} | {'Точная вероятность':<20} | {'Симуляция (10000)':<20}")
    print("-" * 55)
    for p in range(5, 61, 5):
        exact = birthday_probability(p)
        simulated = simulate_birthday(p, 10000)
        print(f"{p:<6} | {exact:<20.5f} | {simulated:<20.5f}")

    print("\n--- Поиск минимального числа людей (> 0.5) ---")
    for p in range(1, 100):
        if birthday_probability(p) > 0.5:
            print(f"Наименьшее число людей, при котором вероятность > 0.5: {p}")
            break