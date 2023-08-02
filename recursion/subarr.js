let pokemons = ['pikachu', 'bulbasaur', ['eevee', ['sylveon', 'glaceon', 'flareon', ['umbreon', 'espeon']]] ,['mew', 'mewtwo']];

function print_values(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      print_values(arr[i])
    }
    else {
      console.log(arr[i])
    }
  }
};

print_values(pokemons);