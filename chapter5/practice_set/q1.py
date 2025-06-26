# 1. Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide user with an option to look it up! 

words = {
    "kaha ho":"where are you",
    "chitra":"pitcher",
    "natak":"pretending"
}

word = input("Enter a world in english to translate :> ")
print(words[word])