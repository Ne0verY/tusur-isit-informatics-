def pasture_area(wire, w):
    if w <= 0 or w >= wire / 2:
        return 0.0
    length = wire - 2 * w
    return w * length

def best_pasture(wire):
    w = wire / 4
    area = pasture_area(wire, w)
    length = wire - 2 * w
    return (w, length, area)

if __name__ == "__main__":
    print(pasture_area(100, 25))
    print(pasture_area(100, 10))
    print(pasture_area(100, 50))
    print(best_pasture(100))
    print(best_pasture(60))
    print(best_pasture(12))