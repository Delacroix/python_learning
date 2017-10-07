def make_shirt(size, style):
    print('\nI want a shirt.')
    print('The shirt\'s size is ' + size +
          ' and style is ' + style.title())
make_shirt('L', 'old_school')
make_shirt(size='XL', style='fashion')

print('============')


def make_shirts(size, style='I love python'):
    print('\nI want a shirt.')
    print('The shirt\'s size is ' + size +
          ' and style is ' + style.title())
make_shirts('XXL')
make_shirts('XXS', 'How to mock')

print('=================')


def describe_city(city_name, country='China'):
    print('\n' + city_name.title() + ' is in ' +
          country.title() + '.')
describe_city('chongqing')
describe_city('chengdu')
describe_city('phuket', 'thailand')