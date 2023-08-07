# sum that sums up all the numbers in a given array

#1. Assume sum has already been implemented
#2. in this case, the subproblem is the array, all the numbers in the array save for the first one
#3. visually think about what happens when we apply the sum function to the sub problem

#Think about it this way where we can just add the first number, 1, to the result of sum[rest of the nums]
# return arr[0] + sum(arr[1:])

pinks = ['pink', 'hot pink', 'floral', 'rose']

#slices from index 1 to second to last element in list
print(pinks[1:-1])

nums = [9,9,9,9,9]

counter = 0

def sum(arr):
    global counter
    counter += 1
    
    if len(arr) == 1:
        print('last call value', arr[0])
        print('recursive function called: ', counter)

        return arr[0]
    print(f'array in this round: {arr[0]} and {arr[0:]}')
    print(f'we are adding: {arr[0]} and {arr[1:]} which is:', arr[0] + sum(arr[1:]))
    return arr[0] + sum(arr[1:])


print(sum(nums))
# print('recursive function called: ', count)


def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])