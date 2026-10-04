def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    print(quick_sort([4, 2, 7, 1, 3, 5]))
    print(quick_sort([7, 3, 3, 4, 1]))
    print(quick_sort([]))