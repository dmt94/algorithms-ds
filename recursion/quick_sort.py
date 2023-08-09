array = [4,3,5,7,9,2,11,6]




    

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
            



