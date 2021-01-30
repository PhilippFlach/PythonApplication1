# UTF-8



foo = 5
float_foo = 5.1
bar = True # False
bee = "Hello World"
boo = 'bye bye'


print(bee + str(foo)) # integers are to be casted into strrings with str() function when printing.
print('what we want to print', end='\n')

names = ['alice','bob']  

names.append('george')
names.append('julia')

length_of_names = len(names) # len()


# ITERABLES
# list, dictionary, tuple -> unmutable list, string


# TERNARY OP (python oneliner)
#new_var = 10 if length_of_name == 10 else 'SOMETHING ELSE'



if length_of_names > 1:
  	print("Hello guys!")
  	for name in names:
         print("Hello " + str(name)+ "!", end='')
elif length_of_name == 1: # else if
   	print("Hello " + str(   names[0]   ))
else:
  	print("There is nobody to greet!")
