file_object = open('myfile.txt', 'r')
print( file_object.read() )
file_object.close()


file_object = open('myfile.txt', 'r')
print( file_object.read(5) )
file_object.close()
OUTPUT
Sampl

file_object = open('myfile.txt', 'r')
for line in file_object:
    print(line)
file_object.close()

with open('myfile.txt', 'r') as file_object :
  file_content = file_object.read()
  print(file_content)

  Note : When we use access mode w and file is not present, 
  Python creates a new file with the given filename. If the file exists already, then the write method will overwrite the file with new data.

#shelve file:
import shelve
with shelve.open('SampleData') as shelfFile:
  courses = ['Python', 'C++', 'Java']
  shelfFile['courses'] = courses    ## Storing data
  print(list(shelfFile.keys()))     ## Retrieving data
  print(list(shelfFile.values()))
