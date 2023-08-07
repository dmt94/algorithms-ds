Calling anagrams_of('abc')               # Calling the function with input 'abc'
  Calling anagrams_of('bc')             # Recursively calling the function with 'bc'
    Calling anagrams_of('c')            # Recursively calling the function with 'c'
      Base case reached: ['c']          # Base case: single character, return ['c']
    Generating anagrams for 'c': ['c']  # Anagrams of 'c' is ['c']
    Iterating over substring 'c'
      Inserting 'b' at index 0: 'bc'   # Insert 'b' at different positions in 'c'
    Iterating over substring anagrams: ['bc']  # Anagrams of 'c' with 'b' at different positions
      Inserting 'a' at index 0: 'abc'  # Insert 'a' at different positions in 'bc'
      Inserting 'a' at index 1: 'bac'
      Inserting 'a' at index 2: 'bca'
  Generating anagrams for 'bc': ['abc', 'bac', 'bca']  # Anagrams of 'bc' with 'a' at different positions
  Iterating over substring 'bc'
    Inserting 'c' at index 0: 'cbc'   # Insert 'c' at different positions in 'bc'
    Inserting 'c' at index 1: 'bcc'
  Iterating over substring anagrams: ['cbc', 'bcc']  # Anagrams of 'bc' with 'c' at different positions
    Inserting 'a' at index 0: 'acbc'  # Insert 'a' at different positions in 'cbc'
    Inserting 'a' at index 1: 'abcc'
    Inserting 'a' at index 2: 'abcc'
    Inserting 'a' at index 3: 'abcc'
Generating anagrams for 'abc': ['acbc', 'abcc', 'abcc', 'abcc', 'abc', 'bac', 'bca', 'cbc', 'bcc']  # Final anagrams of 'abc'
Iterating over substring 'abc'
  Inserting 'c' at index 0: 'cbc'     # Insert 'c' at different positions in 'abc'
  Inserting 'c' at index 1: 'bcc'
  Inserting 'c' at index 2: 'bcc'
Iterating over substring anagrams: ['cbc', 'bcc', 'bcc']  # Anagrams of 'abc' with 'c' at different positions
  Inserting 'a' at index 0: 'acbc'    # Insert 'a' at different positions in 'cbc'
  Inserting 'a' at index 1: 'abcc'
  Inserting 'a' at index 2: 'abcc'
  Inserting 'a' at index 3: 'abcc'
  Inserting 'a' at index 4: 'abcc'
  Inserting 'a' at index 5: 'abcc'
  Inserting 'a' at index 6: 'abcc'
  Inserting 'a' at index 7: 'abcc'
[]