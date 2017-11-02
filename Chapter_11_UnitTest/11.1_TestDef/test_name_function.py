import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """Whether the function can deal with Janis Joplin?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Whether the function can deal with Wolfgang Amadeus Mozart"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
