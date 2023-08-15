def pick_pokemon(pokemons):
    eliminate = "top"

    while len(pokemons) > 1:
        if eliminate == "top":
            pokemons = pokemons[len(pokemons) // 2 : len(pokemons)]
            eliminate = "bottom"
        elif eliminate == "bottom":
            pokemons = pokemons[0:len(pokemons) // 2]
            eliminate = "top"

    return pokemons[0]

water_pokemons = ['squirtle', 'psyduck', 'seel']

print(pick_pokemon(water_pokemons))