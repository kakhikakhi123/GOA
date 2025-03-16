def check_lowercase(user_str):
    if user_str.islower():
        print(user_str)
    else:
        print("The string is not in lowercase.")

text = input("Please enter a sentence: ")
check_lowercase(text)

def iscapitalized(user_str):
    if user_str[0].isupper() and user_str[1:].islower():
        print(True)
    else:
        print(False)

# მომხმარებლის წინადადების შემოყვანა
text = input("გთხოვთ, შეიყვანეთ წინადადება: ")

# ფუნქციის გამოძახება text ცვლადით
iscapitalized(text)

def manual_isdigit(user_str):
    # დარწმუნდით, რომ user_str არის სთრინგი
    if not isinstance(user_str, str):
        return False

    for char in user_str:
        # შეამოწმეთ არის თუ არა სიმბოლო რიცხვი (0-დან 9-მდე)
        if char < '0' or char > '9':
            return False
    
    return True

# შედეგის დაბეჭვდა
test_str = "12345"
print(manual_isdigit(test_str))  # True
test_str2 = "12a45"
print(manual_isdigit(test_str2))  # False

def split_sentence(user_str):
    # სტრინგის დაყოფა სფეისების მიხედვით და მიღებული სიის დაბეჭვდა
    words_list = user_str.split(' ')
    print(words_list)

# მომხმარებლისგან ტექსტის შეყვანა
user_input = input("შეიყვანეთ ტექსტი: ")
split_sentence(user_input)
