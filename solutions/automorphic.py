def is_automorphic(n):
    square_str = str(n * n)
    n_str = str(n)
    return square_str.endswith(n_str)

if __name__ == "__main__":
    print(is_automorphic(25))
    print(is_automorphic(76))
    print(is_automorphic(5))
    print(is_automorphic(13))