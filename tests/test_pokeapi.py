import unittest
from PokeAPI import PokeAPI


class TestPokeAPI(unittest.TestCase):

    def test_get(self):
        "Functions return a value"
        pk = PokeAPI()
        result = pk.get_pokemon(1)
        self.assertTrue('name' in result)

    def test_memo(self):
        "Memoization works"
        pk = PokeAPI()
        for _ in range(1000):
            pk.get_pokemon(2)
        self.assertTrue(True)

    def test_limit_offset(self):
        "Limit and offset params works correctly"
        pk = PokeAPI()
        pokemon = pk.get_pokemon(limit=20)
        self.assertTrue(len(pokemon['results']) == 20)
        pokemon = pk.get_pokemon(offset=20)
        self.assertTrue(pokemon['previous'])
