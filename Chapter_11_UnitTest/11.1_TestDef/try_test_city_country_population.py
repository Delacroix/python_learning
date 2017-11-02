from try_11_1_city_country import city_function
import unittest


class TestCityCase(unittest.TestCase):
    def test_city_country_population(self):
        formatted_name = city_function('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

unittest.main()