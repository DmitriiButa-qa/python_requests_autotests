import requests
import json

token = 'e37726e2f784dceccdda5eeab60d193e'
response = requests.post('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token' : token}, json={
    "name": "Псайдак",
    "photo": "https://avatanplus.com/files/resources/mid/57ad592d371341567d2458aa.png"
})

print(response.text)

response_2 = requests.put('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token' : token}, json={
    "pokemon_id": 2671,
    "name": "Нидорино",
    "photo": "https://www.pngmart.com/files/22/Nidorino-Pokemon-PNG-Pic.png"
})

print(response_2.text)

response_3 = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',headers={'trainer_token' : token}, json={
    "pokemon_id": "2671"
})

print(response_3.text)