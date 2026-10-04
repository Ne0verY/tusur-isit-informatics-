import math

def race(v1, v2, g):
    # Если вторая черепаха не быстрее первой, она никогда её не догонит
    if v2 <= v1:
        return None
    
    # Вычисляем время в часах (дробное число)
    # Формула: расстояние / разница скоростей
    time_in_hours = g / (v2 - v1)
    
    # Переводим время в секунды и округляем до целого
    total_seconds = round(time_in_hours * 3600)
    
    # Вычисляем часы, минуты и секунды
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    
    minutes = remainder // 60
    seconds = remainder % 60
    
    return [hours, minutes, seconds]

print(race(720, 850, 70))  
print(race(820, 81, 550))   
print(race(80, 91, 37))      
print(race(80, 100, 40))   
print(race(720, 850, 370)) 
print(race(820, 850, 550)) 
print(race(100, 100, 50)) 
