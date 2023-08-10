# 1. Write function that returns greatest product of any three numbers using fast sorting that computes at O(N log N)

def greatest_product_of_3(arr):
    arr.sort()

    return arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) -3]

# 2. find missing number in an array

def find_missing_num(arr):
    arr.sort()

    # array can have value that doesnt necessarily have to start at 0
    # make sure end of range is the maximum known value + 1 bc range method is not inclusive 
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            print(i)

find_missing_num([2,5,4,6,7])

arrs = [3,5,4,6,7]


#3 Write 3 diff implementation of a function that finds the greatest number within an array. write one function that is O(N^2), one that is O(N log N), and one that is O(N)

#NOTE O(N^2) Quadratic = nested for loops

def find_max(arr):
    for num in arr:
        max_num = num
        for compare_num in arr:
            if compare_num > num:
                max_num = compare_num
    
    return max_num

print(find_max([4,3,2,44,1]))


#NOTE O(N log N) Sort

def find_max_sort(arr):
    arr.sort()

    return arr[-1]


#NOTE O(N) Sort, loop once

def find_max_loop(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num

print(find_max_loop([6,7,2,3,11,233,100,34]))