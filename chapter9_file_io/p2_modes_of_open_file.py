# MODES OF OPENING A FILE  
'''
r - open for reading 
w - open for writing  
a - open for appending 
+  - open for updating. 
'rb' will open for read in binary mode. 
'rt' will open for read in text mode.
'''

st = "amazing "
f = open("myfils.text", "a")
f.write(st)
f.close