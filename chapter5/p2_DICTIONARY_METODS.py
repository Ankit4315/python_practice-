a= {"name":"ankit" ,
   "from":"india" ,
   "marks":[92,98,96]
   }


# 1• a.items(): Returns a list of (key,value)tuples.
print(a.items())
 
# 2• a.keys(): Returns a list containing dictionary's keys. 
print(a.keys())

# 3• a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
a.update({"from": "mp sir"}) # this will update the value of key
print(a)

a.update({"kon si colony bhai":"gayatri colony bro"})  # this will add the key value in the dictionary
print(a)

# 4• a.get("name"): Returns the value of the specified keys (and value is returned eg."ankit" is returned here). 

print(a.get("india")) # this will return None becouse no key is there in the dicrinary

print(a.get("kon si colony bhai")) # this will return the value of the kye (gayatri colony bro)


# 5 difference bettween accessing element by .get and indexing method 

print(a.get("name2")) # return non
# print(a["name2"]) # return error

# 5 dic.clear : empty the dictionary  6. dic.copy : this shellow copy the dictionarty
b={"name": "ankit", "age":22, "nation": "india"}

c = b.copy()
b.clear()

print(b)
print(c)

# 7 dic.pop(key) : this will remove and return (key,value) pair with the spacific key.
result= c.pop("name")
print(result)
print(c)

#  8 dic.popitem() : this will remove and return (key,value) pair in the LIFO(last-in-first-out) order 
item = c.popitem()
print(item)
print(c)
