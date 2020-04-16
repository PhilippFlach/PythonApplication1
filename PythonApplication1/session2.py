# name = 'Philipp'

# print(name)
# print("Type: " + str(type(name)))

# name = iter(name)
# print("Type: " + str(type(name)))

# # next()

# cursor = next(name)
# print(cursor)


# cursor = next(name)
# print(cursor)


d1 = {'header1': 'value1', 'header2': 'value2'}


for key, value in d1.items(): # ('header1', 'value1') # the tuple unpacked automatically
    print(key, value)


for count, t1 in enumerate(d1.items()): # ('header1', 'value1') # enumerate() # Enumerations made the unpack unable
    print(count, t1[0], t1[1])





