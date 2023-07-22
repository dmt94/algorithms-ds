# sorting in ascending order 
# bubble sort runs on quadratic time, not efficient

def bubble_sort(list):
    # keeps tracks of the rightmost index of the array that has NOT yet been sorted 
    # we are assuming that when we start off, the array is completely unsorted, 
    # so this variable is initialized to be the last index of the array
    
    unsorted_until_index = len(list) - 1
    

    # keep track of whether the array is fully sorted
    sorted = False

    # while loop keeps going while sorted is False
    # sorted will continue to be False if the for loop encounters adjacent values that still need to be swapped
    while not sorted:
        sorted = True
        # loop goes until the index that has not yet been sorted
        for i in range(unsorted_until_index):
        #within this loop, we compare each pair of adjacent values and swap those values if they're out of order
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                # we change the value for sorted back to False if we have to make a swap
                sorted = False
        #at the end of each pass through, we know that the value we bubbled up all the way to the right is now in its correct position, so we decrement the unsorted_until_index by 1, since the index it was already pointing to is now sorted
        unsorted_until_index -= 1

    return list 