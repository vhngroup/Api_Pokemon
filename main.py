import requests

pokemon = input("Que pokemon deseas buscar?").lower()

if pokemon: 
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.status_code==200:
        pokemon_data = response.json()

        name = pokemon_data['name']
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        type = [type_info['type']['name'] for type_info in pokemon_data['types']]

        print(f"_________**Estos son los datos**_______")
        print(f"Nombre: {name.capitalize()}")
        print(f"Altura: {height / 10} m")
        print(f"Peso: {weight / 10} Kg")
        print(f"Tipos: {weight / 10}")

        print("\n Estadisticas Base: ")
        for stat in pokemon_data['stats']:
            stat_name = stat['stat']['name']
            base_stat = stat['base_stat']
            print(f"{stat_name.capitalize()}: {base_stat}")
    else:
        print(f"Error: {response.status_code}, digitaste bien el nombre?")
else:
    pokemon = input("No haz indicado que pokemon buscar. Que pokemon buscas?")