name = 'Philipp'


print(name)
print("Type: " + str(type(name)))

name = iter(name)
print("Type: " + str(type(name)))

# next()

cursor = next(name)
print(cursor)


cursor = next(name)
print(cursor)