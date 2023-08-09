# function accepts an array of numbers that returns the sum, as long as a number doesn't bring the sum above 100. If adding a number will make the sum higher than 100, that number is ignored. Fix fn below to get rid of unnecessary recursivie calls

# def add_until_100(arr):
#     if len(arr) == 0:
#         return 0
    
#     if arr[0] + add_until_100(arr[1:]) > 100:
#         return add_until_100(arr[1:])
#     else:
#         return arr[0] + add_until_100(arr[1:])

def add_until_100(arr):
    if len(arr) == 0:
        return 0
    
    sum_of_remaining = add_until_100(arr[1:])
    
    if arr[0] + sum_of_remaining > 100:
        return sum_of_remaining
    else:
        return arr[0] + sum_of_remaining
    

# 2 Golomb Sequence, following fn calculates the Nth number from math sequeence. Rewrite using memoization to optimize.

# def golomb(n, memo={}):
#     if n == 1:
#         return 1
#     return 1 + golomb(n - golomb(golomb(n-1)))

def golomb(n, memo={}):
    if n == 1:
        return 1
    
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)

    return memo[n]

#3 "Unique Path" with memoization

# def unique_path(rows, cols):
#     if rows == 1 or cols == 1:
#         return 1
    
#     return unique_path(rows - 1, cols) + unique_path(rows, cols - 1) 

def unique_path(rows, cols, memo={}):
    if rows == 1 or cols == 1:
        return 1
    
    if [rows,cols] not in memo:
        memo[rows, cols] = unique_path(rows - 1, cols, memo) + unique_path(rows, cols - 1, memo)
    
    return memo[rows,cols]

