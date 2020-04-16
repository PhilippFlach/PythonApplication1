###################
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
###################



###################
# d1 = {'header1': 'value1', 'header2': 'value2'}


# for key, value in d1.items(): # ('header1', 'value1') # the tuple unpacked automatically
#     print(key, value)


# for count, t1 in enumerate(d1.items()): # ('header1', 'value1') # enumerate() # Enumerations made the unpack unable
#     print(count, t1[0], t1[1])
###################


###################
# reading files
# our_file = open('testdata/linearregression.csv', 'r')
# # print('Type: ' + str(type(our_file)))

# for row in our_file.readlines():
#     print(row, end='')

# our_file.close()
###################


###################
# reading file with 'with' keyword
with open('testdata/linearregression.csv', 'r') as our_file:
    for row in our_file.readlines():
        # print(row, end='')
        seperated = row.split(';')
        item1 = seperated[0]
        item2 = seperated[1]

        item2 = item2[:-1] # item2[0:-1]
        print(item1, item2, sep='---')
###################



