def manual_capitalize(user_str):
    if len(user_str) == 0:
        return user_str
    return user_str[0].upper() + user_str[1:].lower()

# მომხმარებლების შეყვანის მოთხოვნა
user_input = input("შეიყვანეთ სთრინგი: ")

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
capitalized_str = manual_capitalize(user_input)
print("Capitalized სთრინგი: ", capitalized_str)
