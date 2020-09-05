def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        
        if arr[i] == target:
            return i
 
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)
    mid_index = 0
    while start <= end:
        #get the middle point 
        mid_index = (start + end) // 2
           # If target is greater, ignore left half      
        if arr[mid_index] < target:
            start = mid_index + 1
           # If x is smaller, ignore right half 
        elif arr[mid_index] > target:
            end = mid_index - 1
        else: 
            return mid_index
    return -1  # not found


