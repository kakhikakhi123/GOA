# Find
# 2. Find the position of the first occurrence of the word "Python" in a sentence
sentence = "I love learning Python because it's a versatile language."
position = sentence.find("Python")
print(f"The position of the word 'Python' is: {position}")

# 3. Search for a user-specified substring in a provided string and print its starting index
provided_string = "Programming is fun with Python."
substring = input("Enter the substring to search for: ")
index = provided_string.find(substring)
if index != -1:
    print(f"The substring starts at index: {index}")
else:
    print("Substring not found.")

# 4. Write a function to find and return the index of a specified character in a given string
def find_character(string, char):
    return string.find(char)

string = "Learning Python"
char = input("Enter the character to find: ")
print(f"The index of '{char}' is: {find_character(string, char)}")

# Count
# 5. Count the number of times the word "the" appears in a given paragraph
paragraph = "The quick brown fox jumps over the lazy dog. The dog barks at the fox."
word_count = paragraph.lower().count("the")
print(f"The word 'the' appears {word_count} times.")

# 6. Ask the user to input a character and count its occurrences in a given string
user_string = input("Enter a string: ")
user_char = input("Enter a character to count: ")
char_count = user_string.count(user_char)
print(f"The character '{user_char}' appears {char_count} times in the string.")

# 7. Create a function that counts and returns the occurrences of a specified word in a text
def count_word(text, word):
    return text.lower().count(word.lower())

text = "Python is amazing. I love Python!"
word = "Python"
print(f"The word '{word}' appears {count_word(text, word)} times.")

# Index
# 8. Find and print the index of the first occurrence of the word "hello" in a given string
sample_string = "hello world, hello universe"
hello_index = sample_string.find("hello")
print(f"The index of the first occurrence of 'hello' is: {hello_index}")

# 9. Write a function that returns the index of a character provided by the user in a string
def find_user_char(string, char):
    return string.find(char)

string_input = input("Enter a string: ")
char_input = input("Enter a character to find: ")
print(f"The index of '{char_input}' is: {find_user_char(string_input, char_input)}")

# Islower
# 10. Check if all characters in a given string are lowercase and print the result
lowercase_string = "python is fun"
is_all_lower = lowercase_string.islower()
print(f"All characters are lowercase: {is_all_lower}")

# 11. Create a function that takes a string and returns True if it is completely in lowercase, otherwise False
def is_all_lowercase(string):
    return string.islower()

test_string = "coding"
print(f"Is the string all lowercase? {is_all_lowercase(test_string)}")

# 12. Prompt the user to input a string and verify if it contains only lowercase letters
user_lower_string = input("Enter a string: ")
if user_lower_string.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string contains characters that are not lowercase.")

# Isupper
# 13. Verify if all the characters in a user-provided string are uppercase
user_upper_string = input("Enter a string: ")
if user_upper_string.isupper():
    print("All characters are uppercase.")
else:
    print("The string is not fully uppercase.")

# 14. Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result
def is_all_uppercase(string):
    return string.isupper()

test_upper_string = "PYTHON"
print(f"Is the string all uppercase? {is_all_uppercase(test_upper_string)}")

# 15. Check and display whether a string input by the user is in uppercase
input_uppercase_string = input("Enter a string to check for uppercase: ")
if input_uppercase_string.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")
