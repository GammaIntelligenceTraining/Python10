'''
'r' - read
'a' - append
'w' - write
'x' - create
'r+' - read and write
'''
# cp1252
# cp1257
import datetime

with open('text_files/python.jpg', 'rb') as file:
    data = file.read(4096)
    print(data)
    with open('python-logo_copy.png', 'wb') as wfile:
        wfile.write(data)