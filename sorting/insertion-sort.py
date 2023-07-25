def insertion_sort(arr):
    
    # we start a loop at the beginning at index 1 that runs through
    # the entire array
    # each round of this loop represents a "pass-through"
    for idx in range(1, len(arr)):
        
        # within each pass through, we have a value we are "removing"
        # that we are using to compare to the inner loop values
        temp_val = arr[idx]

        # starts immediately to the left of the index of the temp_val
        # position represents EACH VALUE WE COMPARE against the TEMP_VALUE
        position = idx - 1

        
        while position >= 0:
            # we check whether the value at position is greater than the temp_val
            if arr[position] > temp_val:
                # if position left to the temp_val that starts at index 1 is greater than temp_val, we shift the left value to the right, switching with the temp_val position
                arr[position + 1] = arr[position]
                # we then decrement the position -1, but it will never be less than 0 because we set the outer while loop for the position to be greater than or equal to 0
                position = position - 1
            else: 
                break
         
         # the final step of each pass-through is moving the temp_val into the gap    
         # if the position being compared with the temp_val is less than or equal to the temp_val
         # we place the temp_val to the position after it
        arr[position + 1] = temp_val


    return arr


# worst case scenario, we compare and shift all the data and in best case scenario, we shift none of the data. For average scenario, we can say that we probably compare and shift about half the data