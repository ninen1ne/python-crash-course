# 15/5/2024
from city_functions import get_city_country

def test_city_country():
    """Do info like 'Bangkok, Thailand' work?"""
    information = get_city_country('bangkok', 'thailand')
    assert information == 'Bangkok, Thailand'

def test_city_country_population():
    """Do info like 'Santiago, Chile - population 500_000' work"""
    information = get_city_country('santiago', 'chile', 500_000)
    assert information == 'Santiago, Chile - population 500000'
