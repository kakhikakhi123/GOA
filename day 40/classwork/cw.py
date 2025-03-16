# ფუნქციის განსაზღვრა
def greet(name, surname, age, academy, favourite_color, city):
    # f-სთრინგის გამოყენება ტექსტის ფორმატირებისთვის
    return f"Hello, my name is {name}, my surname is {surname}. I am {age} years old. I study in {academy}. My favourite color is {favourite_color}. I live in {city}."

# ფუნქციის გამოყენება და მნიშვნელობის შენახვა
result = greet("Kaxi", "Beridze", 25, "Code Academy", "blue", "Kutaisi")

# შედეგის დაბეჭდვა
print(result)
