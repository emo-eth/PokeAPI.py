# PokeAPI.py
Python wrapper for the v2 of the RESTful API hosted at http://pokeapi.co.  

Each endpoint corresponds to a `get_` method of the wrapper (hyphens replaced with underscores, eg `get_location_area`). To get a list of all endpoints (all of which take an `id or name` as a parameter):  

>from PokeAPI import PokeAPI
>
>pk = PokeAPI()
>
>pk.get_endpoints()

Which returns:

`{'pokemon': 'http://pokeapi.co/api/v2/pokemon/',
  'version': 'http://pokeapi.co/api/v2/version/',
  'location-area': 'http://pokeapi.co/api/v2/location-area/',
  'gender': 'http://pokeapi.co/api/v2/gender/', ...}`  

If not passed an `id` or `name`, each endpoint will return a list of available resources. Each method can take optional `limit` and `offset` parameters, which paginate the listed results accordingly. The default `limit` is 20.  
Calling `pk.get_pokemon()` returns a list of the endpoints of the first 20 Pokémon:  

```{'results':
	[{'url': 'http://pokeapi.co/api/v2/pokemon/1/',
	'name': 'bulbasaur'},
	{'url': 'http://pokeapi.co/api/v2/pokemon/2/',
	'name': 'ivysaur'},
	{'url': 'http://pokeapi.co/api/v2/pokemon/3/',
	'name': 'venusaur'}, ...}```  

To get the next 20 pokemon, call `pk.get_pokemon(limit=20, offset=20)`.  

To get (a lot of) information about `bulbasaur`, call `pk.get_pokemon('bulbasaur')` or `pk.get_pokemon(1)`:  

```{'base_experience': 64, 'is_default': True, 'species': {'url': 'http://pokeapi.co/api/v2/pokemon-species/1/', 'name': 'bulbasaur'}, 'stats': ...}```