

names = ['a','b','c','d','e', 2, 2.3, True, False, ['another','list'], {'key1':'value1', 'key2': 'value2'}, ('this','tuple','is','unmutable')]

for name in names:
    print('Type of my variable is ' + str(type(name)) + ' and the value is ' + str(name))



print('Range of the names list from 3rd element to 6th element: ' + str(  names[2:6]   )) # python list indices

for i in range(1,10,1):
    print(i)