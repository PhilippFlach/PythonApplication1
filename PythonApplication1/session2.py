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

# python -m pip install -U matplotlib
# import matplotlib
###################
# reading files
# our_file = open('testdata/linearregression.csv', 'r')
# # print('Type: ' + str(type(our_file)))

# for row in our_file.readlines():
#     print(row, end='')

# our_file.close()
###################

# PEP 8

###################
# # reading file with 'with' keyword
# with open('PythonApplication1/testdata/linearregression.csv', 'r') as our_file:
#     for row in our_file.readlines():
#         # print(row, end='')
#         seperated = row.split(';')
#         item1 = seperated[0]
#         item2 = seperated[1]

#         item1 = item1[-1] # item2[0:-1]
#         print(item1, item2, sep='---')
#         break
###################



###################
# reading file with csv module
# import csv
# with open('PythonApplication1/testdata/linearregression.csv', 'r') as our_file:
#     our_csv = csv.reader(our_file, delimiter=';')
#     # print("Type: {}, somenumber: {}".format(type(our_csv, 324234324)))

#     for count, row in enumerate(our_csv):
#         if count == 0:
#             item1 = row[0]
#             item2 = row[1]

#             item1 = item1[-1] # item2[0:-1]
#             print(item1, item2, sep='---')
#             continue
#         print(row)
###################



###################
# reading file with csv module
# import csv


# d1 = {} # {'x':[], 'y':[23,23,24546,56,7 ....] }


# with open('PythonApplication1/testdata/linearregression.csv', 'r') as our_file:
#     our_csv = csv.reader(our_file, delimiter=';')

#     for count, row in enumerate(our_csv):
#         if count == 0:
#             item1 = row[0]
#             item2 = row[1]
#             item1 = item1[-1] # item2[0:-1]
#             d1[item1] = []
#             d1[item2] = []
            
#             print(item1, item2, sep='---')
#             continue
#             # exit(1)
        
#         print(row)
#         d1['x'].append(row[0])
#         d1['y'].append(row[1])
    
#     print(d1)
###################


###################
# reading file with csv module AND plotting it with matplotlib
# import csv
# import matplotlib.pyplot as plt


# d1 = {} # {'x':[], 'y':[23,23,24546,56,7 ....] }

# with open('PythonApplication1/testdata/linearregression.csv', 'r') as our_file:
#     our_csv = csv.reader(our_file, delimiter=';')

#     for count, row in enumerate(our_csv):
#         if count == 0:
#             item1 = row[0]
#             item2 = row[1]
#             item1 = item1[-1] # item2[0:-1]
#             d1[item1] = []
#             d1[item2] = []
            
#             print(item1, item2, sep='---')
#             continue
#             # exit(1)
        
#         print(row)
#         d1['x'].append(row[0])
#         d1['y'].append(row[1])
    
#     print(d1)


# #matplotlib comamnd below
# plt.plot(d1['x'],  d1['y'], 'ro')
# plt.ylabel('regressions values')
# plt.xlabel('time')
# plt.show()

###################


###################
import csv

d2 = {}
column1 = []
column2 = []
with open("PythonApplication1/testdata/linearregression.csv", 'r') as fcsv:
    dcsv = csv.DictReader(fcsv, delimiter=';')

    # header = next(dcsv)
    # print(header)
    keys = []

    for row in dcsv:
        keys = list(row.keys())
        print(row)
        print(keys)

        value1 = row[keys[0]]
        value2 = row[keys[1]]

        column1.append(value1)
        column2.append(value2)
        print("{} and {}".format(value1, value2))


d2[keys[0]] = column1
d2[keys[1]] = column2
print(d2)
        