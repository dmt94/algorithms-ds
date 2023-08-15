def isSubset(arr1, arr2):
    hash_table = {}
    largerArr = arr1
    smallerArr = arr2
    

    if len(arr1) < len(arr2):
        smallerArr = arr1
        largerArr = arr2
        
    
    #store all items from largerArr to hash_table
    for val in largerArr:
        hash_table[val] = True

    #iterate through each item in smallerArr and return False if we encounter an item not inside hash_table

    for val in smallerArr:
        if val not in hash_table:
          return False
    
    #if we got this far into our code without returning False, it means that all the items in the smallerArray must be contained within largerArr
    return True

#This approach has a time complexity of O(N + M) to build the hash_table and then check if all elements in smallerArr are present in it. It's more efficient than the original nested loop approach (O(N * M)) for larger arrays, especially when largerArr is much bigger than smallerArr.

#function counts duplicates as a subset, ex: [4,4,4] in [4,5,3,2] is True
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 0]
print(isSubset(arr1, arr2))  # Output: True