from BaseAPI import BaseAPI


class PokeAPI(BaseAPI):
    memo = {}

    def __init__(self):
        super(PokeAPI, self).__init__('http://pokeapi.co/api/v2/',
                                      cache_life=86400)

    def get_endpoints(self, limit=None, offset=None):
        params = self._parse_params(locals().copy())
        query_string = '?'
        return self._get(query_string)

    @BaseAPI._memoize
    def get_location(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'location/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_characteristic(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'characteristic/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pal_park_area(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pal-park-area/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon_color(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon-color/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_ability(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'ability/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_language(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'language/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_version(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'version/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_generation(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'generation/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_stat(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'stat/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_encounter_condition_value(self, id_or_name='', limit=None,
                                      offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'encounter-condition-value/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_category(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-category/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_damage_class(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-damage-class/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_evolution_trigger(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'evolution-trigger/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_encounter_method(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'encounter-method/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_nature(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'nature/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_version_group(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'version-group/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_item_fling_effect(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'item-fling-effect/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_machine(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'machine/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon_form(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon-form/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_battle_style(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-battle-style/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_learn_method(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-learn-method/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_type(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'type/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_super_contest_effect(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'super-contest-effect/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokeathlon_stat(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokeathlon-stat/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_item_category(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'item-category/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon_species(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon-species/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_egg_group(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'egg-group/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_item(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'item/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon_shape(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon-shape/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_berry_flavor(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'berry-flavor/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_item_attribute(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'item-attribute/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_gender(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'gender/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_encounter_condition(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'encounter-condition/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokedex(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokedex/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_evolution_chain(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'evolution-chain/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_location_area(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'location-area/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_contest_type(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'contest-type/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_berry(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'berry/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_contest_effect(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'contest-effect/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_pokemon_habitat(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'pokemon-habitat/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_berry_firmness(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'berry-firmness/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_ailment(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-ailment/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_move_target(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'move-target/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_growth_rate(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'growth-rate/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_item_pocket(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'item-pocket/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)

    @BaseAPI._memoize
    def get_region(self, id_or_name='', limit=None, offset=None):
        params = self._parse_params(locals().copy(), ['id_or_name'])
        query_string = 'region/'
        query_string += str(id_or_name) + '?'
        query_string += params
        return self._get(query_string)


def _make_methods():
    "Automagically generates methods based on the API endpoints"
    for k, v in PokeAPI().get_endpoints().items():
        string = "\t@BaseAPI._memoize\n"
        string += ("\tdef get_{0}(self, id_or_name='', limit=None,"
                   .format(k.replace('-', '_')) + ' offset=None):\n')
        string += ("\t\tparams = self._parse_params(locals().copy(), " +
                   "['id_or_name'])\n")
        string += "\t\tquery_string = '{0}/'\n".format(v.split('/')[-2])
        string += "\t\tquery_string += str(id_or_name) + '?'\n"
        string += '\t\tquery_string += params\n'
        string += '\t\treturn self._get(query_string)\n'
        print(string)


if __name__ == '__main__':
    _make_methods()
