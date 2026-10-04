def index_of_min(values):
    if not values:
        return -1
    
    min_index = 0
    
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
            
    return min_index

if __name__ == "__main__":
    print(index_of_min([10, -3, -5, 2, 5])) 
    print(index_of_min([1, 2, 3]))          
    print(index_of_min([4, 1, 1, 9]))      
    print(index_of_min([]))                 
