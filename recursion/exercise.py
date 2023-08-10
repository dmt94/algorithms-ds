# 1. Write function that returns greatest product of any three numbers using fast sorting that computes at O(N log N)

def greatest_product_of_3(arr):
    arr.sort()

    return arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) -3]

# 2. find missing number in an array

def find_missing_num(arr):
    arr.sort()

    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            print(i)

# find_missing_num([2, 3, 4, 6, 7])


find_missing_num([2,5,4,6,7])

# print(len([2,3,4,6,7]))

arrs = [3,5,4,6,7]
print(arrs[-1] + 1)