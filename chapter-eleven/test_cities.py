# Exercise 11-1 City, Country & Exercise 11-2: Population

import unittest
from city_country import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_country.py'. """

    def test_city_country(self):
        """Checks if City Country is correctly formatted"""
        correct_cc_format = city_country("santiago", "chile")
        self.assertEqual(correct_cc_format, "Santiago, Chile")

    def test_city_country_population(self):
        """Checks if City Country, Population is formatted right"""
        correct_ccp_format = city_country(
            "highland park", "illinois", 29641)
        self.assertEqual(correct_ccp_format, "Highland Park, Illinois -Population: 29641")

unittest.main()