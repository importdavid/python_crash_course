"""Tests to verify functionality of city_functions.py. For use with pytest"""

from city_functions import city_country

def test_city_country():
    s = city_country('santiago', 'chile')
    assert s == 'Santiago, Chile'

def test_city_country_population():
    s = city_country('santiago', 'chile', 5000000)
    assert s == 'Santiago, Chile - population 5000000'