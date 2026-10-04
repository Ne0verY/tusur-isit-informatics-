def are_equivalent(f, g, n):
    for i in range(2 ** n):
        row = []
        for j in range(n - 1, -1, -1):
            row.append(bool((i >> j) & 1))
        row_tuple = tuple(row)
        if f(*row_tuple) != g(*row_tuple):
            return False
    return True

def de_morgan_left(a, b):
    return not (a and b)

def de_morgan_right(a, b):
    return (not a) or (not b)

def wrong(a, b):
    return (not a) and (not b)

def implies(a, b):
    return (not a) or b

if __name__ == "__main__":
    print(are_equivalent(de_morgan_left, de_morgan_right, 2))
    print(are_equivalent(de_morgan_left, wrong, 2))
    
    def dm2_left(a, b): return not (a or b)
    def dm2_right(a, b): return (not a) and (not b)
    print(are_equivalent(dm2_left, dm2_right, 2))
    
    def impl_left(a, b): return implies(a, b)
    def impl_right(a, b): return (not a) or b
    print(are_equivalent(impl_left, impl_right, 2))
    
    def contra_left(a, b): return implies(a, b)
    def contra_right(a, b): return implies(not b, not a)
    print(are_equivalent(contra_left, contra_right, 2))