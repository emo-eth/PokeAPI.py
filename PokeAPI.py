import requests
import json


class RateLimitError(Exception):

    def __init__(self):
        self.value = '403 Error/Rate Limit Encountered'


class APIError(Exception):

    def __init__(self, value):
        self.value = value


class PokeAPI(object):

    _auth = ''  # auth doesn't even appear to be necessary
    _api = 'http://pokeapi.co/api/v2/'
    headers = {'User-Agent': 'PokeAPI.py'}

    '''Helper properties and methods'''

    @property
    def _key(self):
        '''API auth key property'''
        return 'key=' + self._auth

    def _get(self, qstring):
        '''Handles auth, API query, status checking, and json conversion.
        May raise an exception depending on response status code.
        Returns JSON response.

        Args:
            - string qstring: string for API query without auth key
            - string hm_token: user token (or True if using self.hm_token)
            - function requests_fn: appropriate function from the requests
                library (GET, POST, DELETE)'''
        response = requests.get(self._api + qstring, headers=self.headers)
        self._check_status(response)
        return json.loads(response.text)

    def _post(self, endpoint, payload):
        response = requests.post(self._api + endpoint, data=payload)
        self._check_status(response)
        return json.loads(response.text)

    def _delete(self, endpoint, payload):
        response = requests.delete(self._api + endpoint, data=payload)
        self._check_status(response)
        return json.loads(response.text)

    def _param(self, param, value):
        '''Formats a parameter/value pair for html
        Args:
            - param: parameter name
            - value: value for parameter

        Returns correctly formatted parameter/value'''
        if value:
            return param + '=' + str(value) + '&'
        else:
            return ''

    def _limit(self, count):
        '''Formats count parameter'''
        return self._param('limit', count)

    def _offset(self, page):
        '''Formats page parameter'''
        return self._param('offset', page)

    def _limit_offset(self, page, count):
        '''Formats page and count parameters'''
        return self._limit(page) + self._offset(count)

    def _check_status(self, response):
        '''Saves a bit of typing'''
        sc = response.status_code
        # 2xx statuses are all success
        if sc // 100 == 2:
            assert response.text, 'Invalid response from server'
            return
        elif sc == 403:
            raise RateLimitError()
        elif sc == 401:
            response = json.loads(response.text)
            raise APIError(response['error_msg'])
        else:
            raise ValueError('Status code unhandled: ' +
                             str(sc) + ' for URL ' + response.url)

    def get_endpoints(self):
        query_string = ''
        return self._get(query_string)

    def get_move_learn_method(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-learn-method/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon_shape(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon-shape/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_item_fling_effect(self, id_or_name='', limit=None, offset=None):
        query_string = 'item-fling-effect/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move_ailment(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-ailment/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_super_contest_effect(self, id_or_name='', limit=None, offset=None):
        query_string = 'super-contest-effect/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move_category(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-category/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move(self, id_or_name='', limit=None, offset=None):
        query_string = 'move/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_nature(self, id_or_name='', limit=None, offset=None):
        query_string = 'nature/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move_damage_class(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-damage-class/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_encounter_condition(self, id_or_name='', limit=None, offset=None):
        query_string = 'encounter-condition/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon_species(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon-species/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokeathlon_stat(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokeathlon-stat/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_ability(self, id_or_name='', limit=None, offset=None):
        query_string = 'ability/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_version(self, id_or_name='', limit=None, offset=None):
        query_string = 'version/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_version_group(self, id_or_name='', limit=None, offset=None):
        query_string = 'version-group/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_encounter_condition_value(self, id_or_name='', limit=None, offset=None):
        query_string = 'encounter-condition-value/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_machine(self, id_or_name='', limit=None, offset=None):
        query_string = 'machine/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_location_area(self, id_or_name='', limit=None, offset=None):
        query_string = 'location-area/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_type(self, id_or_name='', limit=None, offset=None):
        query_string = 'type/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_egg_group(self, id_or_name='', limit=None, offset=None):
        query_string = 'egg-group/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_language(self, id_or_name='', limit=None, offset=None):
        query_string = 'language/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon_form(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon-form/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokedex(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokedex/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_item_attribute(self, id_or_name='', limit=None, offset=None):
        query_string = 'item-attribute/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_item_pocket(self, id_or_name='', limit=None, offset=None):
        query_string = 'item-pocket/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_contest_type(self, id_or_name='', limit=None, offset=None):
        query_string = 'contest-type/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon_habitat(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon-habitat/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_generation(self, id_or_name='', limit=None, offset=None):
        query_string = 'generation/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_contest_effect(self, id_or_name='', limit=None, offset=None):
        query_string = 'contest-effect/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pal_park_area(self, id_or_name='', limit=None, offset=None):
        query_string = 'pal-park-area/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_berry_flavor(self, id_or_name='', limit=None, offset=None):
        query_string = 'berry-flavor/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move_target(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-target/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_evolution_trigger(self, id_or_name='', limit=None, offset=None):
        query_string = 'evolution-trigger/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_move_battle_style(self, id_or_name='', limit=None, offset=None):
        query_string = 'move-battle-style/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_pokemon_color(self, id_or_name='', limit=None, offset=None):
        query_string = 'pokemon-color/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_characteristic(self, id_or_name='', limit=None, offset=None):
        query_string = 'characteristic/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_growth_rate(self, id_or_name='', limit=None, offset=None):
        query_string = 'growth-rate/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_item_category(self, id_or_name='', limit=None, offset=None):
        query_string = 'item-category/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_gender(self, id_or_name='', limit=None, offset=None):
        query_string = 'gender/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_berry(self, id_or_name='', limit=None, offset=None):
        query_string = 'berry/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_stat(self, id_or_name='', limit=None, offset=None):
        query_string = 'stat/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_encounter_method(self, id_or_name='', limit=None, offset=None):
        query_string = 'encounter-method/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_region(self, id_or_name='', limit=None, offset=None):
        query_string = 'region/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_berry_firmness(self, id_or_name='', limit=None, offset=None):
        query_string = 'berry-firmness/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_item(self, id_or_name='', limit=None, offset=None):
        query_string = 'item/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_location(self, id_or_name='', limit=None, offset=None):
        query_string = 'location/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)

    def get_evolution_chain(self, id_or_name='', limit=None, offset=None):
        query_string = 'evolution-chain/'
        query_string += id_or_name + "?"
        query_string += self._limit_offset(limit, offset)
        return self._get(query_string)


def make_methods():
    "Automagically generates methods based on the API list default"
    for k, v in PokeAPI().get_endpoints().items():
        string = '\tdef get_{0}(self, id_or_name='', limit=None, offset=None):\n'.format(
            k.replace('-', '_'))
        string += '\t\tquery_string = \'{0}/\'\n'.format(v.split('/')[-2])
        string += '\t\tquery_string += id_or_name + "?"\n'
        string += '\t\tquery_string += self._limit_offset(limit,offset)\n'
        string += '\t\treturn self._get(query_string)\n'
        print(string)
