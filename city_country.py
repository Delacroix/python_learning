def city_country(city_name, country):
    full_name = city_name + ',' + country
    return full_name.title()
city_1 = city_country('chongqing', 'china')
city_2 = city_country('chengdu', 'china')
city_3 = city_country('santiago', 'chile')
print(city_1)
print(city_2)
print(city_3)