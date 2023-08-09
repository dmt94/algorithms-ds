# loop checks each value of an array, if a value is a list, 
# we recursively call the function, passing that value (the subarray, a list) as an argument
# if a value is not a subarray, then it simply prints that value

pokemons = ['pikachu', 'bulbasaur', ['eevee', ['sylveon', 'glaceon', 'flareon', ['umbreon', 'espeon']]] ,['mew', 'mewtwo']]

def print_values(arr):
    for val in arr:
        #array is an instance of                                an object
        #a built-in function in Python that is used to check whether an object is an instance of a particular class or a subclass of that class.
        if isinstance(val, list):
            print_values(val)
        else:
            print(val)

print_values(pokemons)