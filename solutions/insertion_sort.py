def insertion_sort(arr):
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

if __name__ == "__main__":
    print(insertion_sort([4, 2, 7, 1, 3, 5]))
    print(insertion_sort([7, 3, 3, 4, 1]))
    print(insertion_sort([]))