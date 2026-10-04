def truth_table(n):
    result = []
    for i in range(2 ** n):
        row = []
        for j in range(n - 1, -1, -1):
            bit = (i >> j) & 1
            row.append(bool(bit))
        result.append(tuple(row))
    return result

if __name__ == "__main__":
    print(truth_table(1))
    print(truth_table(2))
    print(truth_table(3))
    print(truth_table(0))