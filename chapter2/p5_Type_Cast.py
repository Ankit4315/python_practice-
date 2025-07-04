# type() function is used to find the data type of a given variable in python.

a = 31
t= type(a) # class <int>
print(t)

b = "31"
t = type (b) # class <str>
print(t)

a = "33.2"
print(type(a))
b = float(a)
print(type(b))

# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion