# selection sort is more efficient than bubble sort, but they are still both have
# a quadratic time complexity

# even though selection sort is (N^2 / 2) we ignore constants in Big O Notation

# we are finding the next lowest value each round and 
# swapping it with the current outer loop index position

def selection_sort(arr):
    # each pass through, it uses the variable idx to point to each value of the array
    # goes up to the second-to-last value (len(arr) - 1)
    for idx in range(len(arr) - 1):
        #the lowest_num_idx is 0 at the beginning of the first pass through, 1 at the second...etc.
        lowest_num_idx = idx
        print('outer loop running at idx:', idx)

        for next_idx in range(idx + 1, len(arr)):
            print("inner loop running at idx", next_idx)
            if arr[next_idx] < arr[lowest_num_idx]:
                lowest_num_idx = next_idx


        # if the lowest value is not in its correct position, we perform a swap
        # we swap the lowest value with the value at next_idx

        if lowest_num_idx != idx:
            temp = arr[idx]
            arr[idx] = arr[lowest_num_idx]
            arr[lowest_num_idx] = temp
            print("lowest value this round is:", arr[idx])

    return arr


print(selection_sort([4,3,2,10,5,7]))