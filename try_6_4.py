glossory = {
    'del': 'delete something',
    'title': 'ensure the first letter is upper',
    'set': 'combine a set of replicated items',
    'sort': 'make sure the items are sorted'
}

for name in glossory.keys():
    print(name.title())
    if name in glossory:
        print("  Hi " + name.title() +
              " means '" + glossory[name].title() + "'!")
print("====================Rivers======================")
rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'mississippi river': 'america'
}
for river in rivers.keys():
    print(river.title() + " runs through " + rivers[river].title())
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

print("=========================================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

invited = ['erin', 'dan', 'jen', 'sarah', 'edward', 'phil']

#invite everyone
for name in invited:
    print(name.title())
#check if they have taken the poll
    if name in favorite_languages.keys():
        print("Thank you for taking the poll! Your favorite language is " +
              favorite_languages[name])
#if someone haven't taken the poll, then invite
    else:
        print(name.title() + ", please take the poll!")


