'''
json module provides direct methods for encoding and decoding JSON data.

dump() — reads file-like object and dumps into JSON file.
dumps() — reads object in string format and dumps into JSON file.
load() — reads JSON data and creates object .
loads() — reads JSON data in string format and creates object.
'''

import json
 
## Following is the example of JSON data. 
data1 = {
            'CommonLounge' : {
                'course' : 'Python 3',
                'topic'  : 'File i/o'
            }
        }
with open("data_file.json", "w") as write_file:
    json.dump(data1, write_file)                  ## Dumping JSON data into a file
 
with open("data_file.json", "r") as read_file:
    data_loaded = json.load(read_file)            ## Reading JSON data
    print(data_loaded)
OUTPUT
{'CommonLounge': {'course': 'Python 3', 'topic': 'File i/o'}}


I/O Exceptions
try: 
  with open('myfile.txt', 'r') as file_object :
    file_data = file_object.read() 
except IOError as e:
  print ("I/O Error : ", e.errno, e.strerror)
  
