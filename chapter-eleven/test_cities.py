# Exercise 11-1 City, Country

import unittest
from city_country import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_country.py'. """

    def test_city_country(self):
        """Checks if City Country is correctly formatted"""
        correct_cc_format = city_country("santiago", "chile")
        self.assertEqual(correct_cc_format, "Santiago, Chile")

unittest.main()