# list of values need to be numerical 

def hasDuplicateValue(arr):
    existing_numbers = {}
    for num in arr:
        if num in existing_numbers:
            #checks if the num is already a KEY in the dictionary existing_numbers
            #keys are unique
            return True
        else:
            existing_numbers[num] = True

    return False


numbers = [2,2,4,4,8]
number_2 = [5,3,2,1,4,2]
unique = [11,2,3,411,900,421]

print(hasDuplicateValue(number_2))


# we are using array index values, which are unique to track encountered values
# in the array input
# say we encounter the value 4 in the array input, we will mark a "1" at index 4 in an empty array
# we will note the value of the array input and use that as an index in the empty array