def anagrams_of(str):
    #base case of the recursive function, checks if the length of the input string is equal to 1. If it is, the function returns the single character str[0]

    #efficiency: O(1) bc it only involves a single comparison
    if len(str) == 1:
        return str[0]
    

    #this empty list will store the generated anagrams
    collection = []

    #recursively calls the anagrams_of() function on the substring starting from the second character, which effectively reduces the problem size
    #recursion depth is proportional to the length of the input string, so the time complexity is O(n), where n is the length of input string
    substr_anagrams = anagrams_of(str[1:])

    #iterate over each substring
    # 
    for substring in substr_anagrams:
        #iterate over each index of the substring, from 0 until one index past the end of the string
        for i in range(len(substring) + 1):
            new_anagram = substring[:i] + str[0] + substring[1:]
            collection.append(new_anagram)
    
    return collection


print(anagrams_of('abcd'))




for i in range(len(['1', '2', 3]) + 1):
    print(i)