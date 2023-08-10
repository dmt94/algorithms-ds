def partition(arr, left_pointer, right_pointer):
    
    pivot_index = right_pointer
    pivot = arr[pivot_index]

# we start the right pointer to the left of the pivot, this refers to the index
    right_pointer -= 1

    while True:
        # move the left pointer to the right as long as it points to a value that is LESS THAN the pivot
        while arr[left_pointer] < pivot:
            left_pointer += 1 
        while arr[right_pointer] > pivot:
            right_pointer -= 1

        #check if stop conditions are met, if left pointer has reached the right pointer, if so then we stop and swap the pivot later
        if left_pointer >= right_pointer:
            break       
        # if left pointer is still to the left of the right pointer, we swap the vals of the left and right pointers
        else:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1
        
    arr[left_pointer], arr[pivot_index] = arr[pivot_index], arr[left_pointer]

    # left_pointer is what will be needed for the quicksort algo
    return left_pointer
            

# NOTE that kth_lowest_val represents an index value, 0 = lowest value in an unsorted array, 1 = second lowest, etc. 

def quickselect(arr, kth_lowest_val, left_idx, right_idx):
    # if we reach a base case (subarray has one cell), we know we've found the value we're looking for 
    if right_idx - left_idx <= 0:
        return arr[left_idx]

    # partition the array and grab the index of the pivot
    pivot_index = partition(arr, left_idx, right_idx)

    #if what we are looking for is to the left of the pivot
    if kth_lowest_val < pivot_index:
        #recursively perform quickselect on the subarray to the left of the pivot
        return quickselect(arr, kth_lowest_val, left_idx, pivot_index - 1)
    elif kth_lowest_val > pivot_index:
        #recursively perform quickselect on the subarray to the riht of the pivot
        return quickselect(arr, kth_lowest_val, pivot_index + 1, right_idx)   
    else:
        # if kth_lowest_val == pivot_idx
        # if after the partition, the pivot position is in the same spot as the kth lowest val, we found the val we are looking for
        return arr[pivot_index]

nums = [0, 50, 20, 10, 60, 30]

# NOTE arguments: 
# nums = array the method will perform the quick select on, 
# 1 = index of second to lowest value in array
# 0 = left index pointer (first index of array)
# len(nums) - 1 = right index pointer (last index of array)
print(quickselect(nums, 1, 0, len(nums) - 1))