planet_list = ['mercury', 'mars']

# use append to add Jupiter and Saturn to the end of the list:
planet_list.append('jupiter')
planet_list.append('saturn')
print('List of planets: ', planet_list)

# use extend to add another list to our list:
last_planets = ['uranus', 'neptune']
planet_list.extend(last_planets)
print('Longer list of planets: ', planet_list)

# use insert to add Earth and Venus in the right order:
planet_list.insert(1, "venus")
planet_list.insert(2, "earth")
print('Even more planets: ', planet_list)

# use append to add Pluto:
planet_list.append('pluto')
print('Nine planets: ', planet_list)

# slice the list to make a new list of rocky planets:
one = planet_list.pop(0)
two = planet_list.pop(0)
three = planet_list.pop(0)
four = planet_list.pop(0)
rocky_planets = [one, two, three, four]
print('List of rocky planets: ', rocky_planets)

# use del to remove pluto:
del planet_list[4]
print('Pluto is now gone: ', planet_list)


# Challenge===================================

# list of tuples:


eight_planets = ['mercury', 'venus', 'earth',
                 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

spacecrafts = [('cassini', 'saturn'), ('phoenix', 'mars'), ('juno', 'jupiter')]

for planet in eight_planets:
  if any(planet == item[1] for item in spacecrafts):
    for spacecraft in spacecrafts:
      planet_explorer = spacecraft[0]
      print(planet, 'was explored with ', planet_explorer)
  else:
      print('No exploration for ', planet)





