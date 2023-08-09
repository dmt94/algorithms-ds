import math

result = math.factorial(3)

# Using LOOPS
def factorial_loop(num): 
    product = 1
    for number in range(1, num+1):
        product *= number
    return product


print(factorial_loop(6))


# 5 * 4 * 3 * 2 * 1

# Using RECUSION
#The function factorial_rec takes an integer num as its input.
def factorial_rec(num):
    #base case defined by the condition if num == 1:. When num reaches 1, the function returns 1, as the factorial of 1 is defined to be 1.
    if num == 1:
        return 1
    #If the base case is not met (i.e., if num is greater than 1), the function enters the else block.
    else:          
      # Inside the else block, the function recursively calls itself twice: factorial_rec(num) and factorial_rec(num - 1). This is a key part of the recursion. Each recursive call reduces the value of num by 1.
      return factorial_rec(num) * factorial_rec(num - 1)
      #The return statement multiplies the result of factorial_rec(num) by the result of factorial_rec(num - 1). This is how the factorial of num is computed. The recursive calls continue until the base case is reached (when num becomes 1), at which point the recursion starts to "unwind" and the multiplication operations are performed to calculate the final result.