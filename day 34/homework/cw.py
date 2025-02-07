# 2) წინადადების uppercase ფორმატში გადაყვანა და დაბეჭდვა
sentence = "This is a sample sentence."
print(sentence.upper())

# 3) მომხმარებლის სახელის შემოტანა და uppercase ფორმატში დაბეჭდვა
name = input("შეიყვანეთ თქვენი სახელი: ")
print(name.upper())

# 4) ფუნქცია, რომელიც იღებს სთრინგების სიას და თითოეულს uppercase ფორმატში ბეჭდავს
def print_uppercase(strings_list):
    for string in strings_list:
        print(string.upper())

strings = ["first string", "second string", "third string"]
print_uppercase(strings)

# 5) წინადადების lowercase ფორმატში გადაყვანა და დაბეჭდვა
sentence = "This is a SAMPLE Sentence."
print(sentence.lower())

# 6) მომხმარებლის მეილის შემოტანა და lowercase ფორმატში დაბეჭდვა
email = input("შეიყვანეთ თქვენი მეილი: ")
print(email.lower())

# 7) ფუნქცია, რომელიც იღებს სთრინგს და lowercase ფორმატში ბეჭდავს
def print_lowercase(string):
    print(string.lower())

text = "This is another SAMPLE Sentence."
print_lowercase(text)

# 8) მომხმარებლის სიტყვას capitalize ფორმატში გადაყვანა
word = input("შეიყვანეთ სიტყვა: ")
print(word.capitalize())

# 9) ფუნქცია, რომელიც იღებს სთრინგს და capitalize ფორმატში ბეჭდავს
def print_capitalize(string):
    print(string.capitalize())

text = "this is yet another sample sentence."
print_capitalize(text)
