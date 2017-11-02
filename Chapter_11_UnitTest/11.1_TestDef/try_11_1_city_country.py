def city_function(city, country, population=''):
    if population:
        result = city.title() + ', ' + country.title() + " - population " + str(population)
    else:
        result = city.title() + ', ' + country.title()
    return result
