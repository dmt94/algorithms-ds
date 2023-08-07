# 1 write a function that accepts an array of strings and returns the total number of characters across all the strings

def rf_count_str(arr):
    count = 0
    
    if len(arr) == 0:
      return 0
    
    # base case
    if len(arr) == 1:
      count += len(arr[0])
      return count
    
    else:
      #the strucure, what are you adding up to, usually there is the original input's first element value that you utilize in this step
      count += len(arr[0]) + rf_count_str(arr[1:])
      return count
    

print(rf_count_str(['a', 'bc']))


def loop_count_str(arr):
   count = 0

   #edge case handling
   if len(arr) == 0:
      return []
   
   #nested for loop, O(n^2) = quadratic time complexity
   for str in arr:
      for char in str:
        count += 1
   return count

print(loop_count_str(['a', 'aaa'])) # expected output: 4

###### 

#2 write function that accepts an array of numbers and returns a new array containing just the even numbers

def rec_just_even(arr):
   #always remember to handle edge cases
   if len(arr) == 0:
      return []
   
   #base case, if array is truncated down to only having one element
   # this is what gets returned to the sum call in line 58
   if len(arr) == 1:
      if arr[0] % 2 == 0:
         return [arr[0]]
      else:
         return []
      
  #recursive case
   if arr[0] % 2 == 0:
        # If even, include it in the result and continue with the rest of the array
      return [arr[0]] + rec_just_even(arr[1:])
   
        # If not even, skip it and continue with the rest of the array
   else:
      return rec_just_even(arr[1:])
         

# linear time complexity
def even_only(arr):
   new_arr = []
   for num in arr:
      if num % 2 == 0:
         new_arr.append(num)

   return new_arr

