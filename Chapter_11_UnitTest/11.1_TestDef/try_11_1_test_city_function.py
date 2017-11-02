from try_11_1_city_country import city_function
import unittest

class CityTestCast(unittest.TestCase):
    """test city function"""
    def test_city_country(self):
        formatted_name = city_function('chongqing', 'china')
        self.assertEqual(formatted_name, 'Chongqing, China')

unittest.main()