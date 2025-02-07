def greet(name):
    print(f"გამარჯობა {name}!")

# ფუნქციის გამოძახება ხუთჯერ სხვადასხვა სახელით
greet("მარიამ")
greet("გიორგი")
greet("ნინო")
greet("ლევან")
greet("თამარ")

def multiply(num1, num2):
    print(f"{num1} გამრავლებული {num2}-ზე არის {num1 * num2}")

# ფუნქციის გამოძახება ხუთჯერ სხვადასხვა არგუმენტებით
multiply(2, 3)
multiply(4, 5)
multiply(6, 7)
multiply(8, 9)
multiply(10, 11)

def my_range(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)

# ფუნქციის გამოძახება ხუთჯერ სხვადასხვა არგუმენტებით
my_range(1, 5)
my_range(10, 15)
my_range(20, 25)
my_range(30, 35)
my_range(40, 45)
