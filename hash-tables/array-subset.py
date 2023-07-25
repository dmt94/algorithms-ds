# determine whether an array is a subset of another array

# O(N * M) time efficiency:

def isSubset(arr1, arr2):
    #determine which array is smaller
    largerArr = arr1
    smallerArr = arr2

    if len(arr1) < len(arr2):
      largerArr = arr2
      smallerArr = arr1
    
    #iterate through smaller array first
    for i in smallerArr:
       foundMatch = False
       #for each smaller array iterate through larger array
       for j in largerArr:
          if i == j:
             foundMatch = True
             break
    if foundMatch == False:
      return False
    

    return True

print(isSubset([5,5,55,5], [1,2,2,3]))

#using sets
def isSubset(arr1, arr2):
    # Convert arrays to sets to take advantage of set operations
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Check if set2 is a subset of set1
    return set2.issubset(set1)

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5]
print(isSubset(arr1, arr2))  # Output: True
#This approach has a time complexity of O(N + M) since converting lists to sets takes linear time, and the issubset() operation is typically efficient, taking time proportional to the size of the set being checked.

#Using sets to determine if one array is a subset of another is generally more efficient than a nested loop approach, especially for larger arrays.