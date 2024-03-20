import requests
import json

while True:
    chosen_pokemon = input("Enter the name of your chosen Pokemon! ")
    chosen_pokemon = chosen_pokemon.lower()

    url = f'https://pokeapi.co/api/v2/pokemon/{chosen_pokemon}'

    req = requests.get(url)
    if req.status_code == 200:
        pokemon_data = req.json()

        print(f"You chose {pokemon_data['name']}!")

        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(ability['ability']['name'])

        print("Held items:")
        for item in pokemon_data['held_items']:
            print(item['item']['name'])
    else:
        print("Chosen pokemon doesn't exist!")