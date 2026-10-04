def is_balanced_number(n):
    s = str(n)
    length = len(s)
    mid = length // 2
    
    if length % 2 == 0:
        left = s[:mid]
        right = s[mid:]
    else:
        left = s[:mid]
        right = s[mid+1:]
        
    sum_left = sum(int(d) for d in left)
    sum_right = sum(int(d) for d in right)
    
    if sum_left == sum_right:
        return "Balanced"
    else:
        return "Not Balanced"

if __name__ == "__main__":
    print(is_balanced_number(7))
    print(is_balanced_number(59))
    print(is_balanced_number(295591))
    print(is_balanced_number(424))
    print(is_balanced_number(13623))
    print(is_balanced_number(56239814))