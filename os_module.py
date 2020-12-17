import os
## Assigning the current path to a local variable ###
curr_path = os.getcwd()
 
print(curr_path)
print(os.listdir())


print(os.listdir())
os.mkdir('misc')
print(os.listdir())
OUTPUT
['jdoodle.py', 'whitespace.pl']
['jdoodle.py', 'misc', 'whitespace.pl']

# Check if jdoodle.py is present in the current path
print (os.path.isfile('jdoodle.py'))
 
# Check if file_1.py is present in the path
print (os.path.isfile('/home/file_1.py'))
True
False

# List the content of directory
print(os.listdir('.'))
 
# Removing the file
os.remove('jdoodle.py')
 
# List the contents after removal
print(os.listdir('.'))
