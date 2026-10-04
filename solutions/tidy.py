def is_tidy(n):
    s = str(n)
    return s == ''.join(sorted(s))

if __name__ == "__main__":
    print(is_tidy(12))
    print(is_tidy(32))
    print(is_tidy(13579))
    print(is_tidy(2335))
    print(is_tidy(7))