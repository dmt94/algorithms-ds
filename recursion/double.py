#using loops

nums = [2,3,4,5,6]

def double_array(arr):
    index = 0

    while (index < len(arr)):
        arr[index] *= 2
        index += 1

#manipulates the original array using loop
double_array(nums)
print(nums)

# creates a new array from the original array
def double_arr_copy(arr):
    copy = []

    for num in arr:
        copy.append(num * 2)
    
    return copy

new_nums = [1,2,3,4,5]

print(double_arr_copy(new_nums))
print(new_nums)




#USING RECURSION

# MUTATES ORIGINAL ARRAY
new_num = [2,3,4,5]
# in each successive call, we pass in the array again as the first argument, but we also pass along an incremented index

def double_arr_recursion(arr, idx):
    #changes the value of array in each callback
    if idx >= len(arr):
        return
    arr[idx] += 2
    double_arr_recursion(arr, idx + 1)

double_arr_recursion(new_num, 0)

print(new_num)


# CREATES A COPY OF ARRAY
do_not_mutate = [3,4,5,6,7]

def double_arr_copy_recursion(arr, idx):
    # The base case is checked using the condition if idx >= len(arr):. If the index idx is greater than or equal to the length of the array arr, it means we have processed all elements, so an empty list is returned to terminate the recursion.
    if idx >= len(arr):
      return []
    new_val = arr[idx] + 2
    rest_of_arr = double_arr_copy_recursion(arr, idx + 1)
    
    return [new_val] + rest_of_arr
    #The function returns a new list constructed by concatenating [new_val] (which is a list containing the computed new value) with the rest_of_array. This step effectively constructs the new array by appending the new value to the result of the recursive call.


print(double_arr_copy_recursion(do_not_mutate,0))
print(do_not_mutate)