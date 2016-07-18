# PokeAPI.py
Python wrapper for the v2 of the RESTful API hosted at (http://pokeapi.co).  

Each endpoint corresponds to a `get_` method of the wrapper. To get a list of all endpoints (all of which take an id or name as a parameter):  

```from PokeAPI import PokeAPI

pk = PokeAPI()

pk.get_endpoints()```

Returns a result of:

`{'pokemon': 'http://pokeapi.co/api/v2/pokemon/',
  'version': 'http://pokeapi.co/api/v2/version/',
  'location-area': 'http://pokeapi.co/api/v2/location-area/',
  'gender': 'http://pokeapi.co/api/v2/gender/', ...}`  

If not passed an `id` or `name`, each endpoint will return a list of available resources. Each method can take optional `limit` and `offset` parameters, which paginate the listed results accordingly. calling `pk.get_pokemon()` returns a list of the first 20 Pokémon:  

```{'results':
	[{'url': 'http://pokeapi.co/api/v2/pokemon/1/',
	'name': 'bulbasaur'},
	{'url': 'http://pokeapi.co/api/v2/pokemon/2/',
	'name': 'ivysaur'},
	{'url': 'http://pokeapi.co/api/v2/pokemon/3/',
	'name': 'venusaur'}, ...}```
