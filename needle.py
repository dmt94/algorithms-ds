# This line defines a function named find_needle that takes two parameters: needle (the substring to find) and haystack (the string in which to search for the needle).
def find_needle(needle, haystack):
    
    #if we can't assume that the haystack is longer length than needle
    if len(haystack) < len(needle):
        return False
    
    #These two lines initialize the variables needle_idx and haystack_idx to 0. These variables will be used to keep track of the positions while traversing the needle and haystack strings, respectively.
    needle_idx = 0
    haystack_idx = 0

    #This is the start of the outer while loop. It ensures that the search continues as long as the haystack_idx is within the valid range of the haystack string.
    while haystack_idx < len(haystack):
        
        #This if statement checks if the character at the current position of needle (indicated by needle_idx) is equal to the character at the current position of haystack (indicated by haystack_idx). If they are the same, it sets found_needle to True.
        if needle[needle_idx] == haystack[haystack_idx]:
            found_needle = True


      # This is the start of the inner while loop. It ensures that the substring comparison continues as long as the needle_idx is within the valid range of the needle string.
        while needle_idx < len(needle):

          #Inside the inner while loop, this if statement checks if the characters at the corresponding positions in needle and haystack are not the same. If that happens, it sets found_needle to False and breaks out of the inner loop since the current position in haystack is not part of the needle.
          if needle[needle_idx] != haystack[haystack_idx + needle_idx]:
              found_needle = False
              break
          
          # If the characters are the same, it increments needle_idx to check the next character in the needle string.
          needle_idx += 1


        # After the inner while loop completes, it checks if found_needle is True, indicating that the entire needle has been found in the haystack. If so, it returns True, indicating a successful match.
        if found_needle == True:
            return True
        
        # If the entire needle is not found at the current position, this line resets needle_idx to 0, and the search continues by incrementing haystack_idx.
        needle_idx = 0

        haystack_idx += 1

    return False


print(find_needle('asdfsafafafd', 'haystack'))

# Analysis
# in worst case scenario, theh algorithm runs for 
# the number of chars in the "needle" * number of chars in "haystack"
# since they both may have diff number of chars then it is O(N*M)