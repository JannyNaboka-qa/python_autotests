import requests

host= 'https://pokemonbattle.me:9104'
token= 'daa7c7d4b3d934ee8cc1710a1156ad82'
response_create = requests.post(f'{host}/pokemons',
                  json=        { "name": "Pytonяш", 
                                 "photo": "https://dolnikov.ru/pokemons/albums/029.png"
}, headers= {"Content-Type":"application/json", "trainer_token":f"{token}"})
print(response_create.text)
id=response_create.json()['id']

response_rename= requests.put(f'{host}/pokemons', json=
                              {
    "pokemon_id": f"{id}",
    "name": "Питоняш",
    "photo": "https://dolnikov.ru/pokemons/albums/047.png"
}, headers= {"Content-Type":"application/json", "trainer_token":f"{token}"})
print(response_rename.text)

response_pokeball= requests.post(f'{host}/trainers/add_pokeball', json=
                                 {
    "pokemon_id": f"{id}"
}, headers= {"Content-Type":"application/json", "trainer_token":f"{token}"})
print(response_pokeball.text)