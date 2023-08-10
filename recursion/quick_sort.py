array = [4,3,5,7,9,2,11,6]
nums = [4,3,2,6,22,32,19,21,7,9,14]

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
            



def quicksort(arr, left_idx, right_idx):
    
    #base case: right index and left index are the same, no movements left
    if (right_idx - left_idx) <= 0:
        return 
    
    #partition the range of elements and grab the index of the pivot:
    pivot_idx = partition(arr, left_idx, right_idx)

    #recursively call the quicksort method on whatever is to the left of the pivot
    quicksort(arr, left_idx, pivot_idx - 1) #we are calling on this sub array

    #recusively call on the right subarray of the pivot
    quicksort(arr, pivot_idx+1, right_idx)


quicksort(array, 0, len(array) - 1)
quicksort(nums, 0, len(nums) - 1)
print(array)
print(nums)