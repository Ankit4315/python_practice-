# 1. len () function – This function returns the length of the strings.

name = "ankit"
print("lent of string :> ",len(name))

# 2. String.endswith("it") – This function_ tells whether the variable string ends with the string "it" or not.
# If string is "ankit", it returns true for "it" since ankit ends with it.

print(name.endswith("it")) #true
print(name.endswith("iti")) #false

print(name.startswith("an")) #true
print(name.startswith("ant")) #false

# 3. string.count("c") – counts the total number of occurrences of any character.

str = "ankit"
count = str.count("r")
print(count) # Output: 0
print(str.count('a')) # Output: 1

# 4. the first character of a given string.
str = "ankit"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Ankit"

# 5. string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string.
str = "ankit"
index = str.find("I")
print(index) # Output: 3 #it return 3 becouse it find the index of i if the velue is not present in the string thne it return -1 and its is case sensitive


# 6. string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.

str = "ankit"
replaced_string = str.replace("t", "i")
print(replaced_string) # Output: "ankii"

re = str.replace("ankit","goolu")  #it aslo replce the whole string 
print(re) # output: "goolu"