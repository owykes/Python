from city_functions import city_country

def test_city_country():
    city = city_country('Portsmouth', 'England')
    assert city == 'Portsmouth, England'