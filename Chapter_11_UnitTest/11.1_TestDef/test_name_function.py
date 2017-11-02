import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """Whether the function can deal with Janis Joplin?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

