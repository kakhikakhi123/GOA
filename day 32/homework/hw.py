def sum_of_two_numbers(a, b):
    print("ჯამი:", a + b)

# ფუნქციის გამოძახება
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
sum_of_two_numbers(num1, num2)

def reverse_string(s):
    return s[::-1]

# ფუნქციის გამოძახება
user_str = input("შეიყვანეთ სთრინგი: ")
print("შებრუნებული სთრინგი:", reverse_string(user_str))

def find_maximum(numbers):
    return max(numbers)

# ფუნქციის გამოძახება
numbers = [3, 5, 7, 2, 8, 10]
print("მაქსიმალური მნიშვნელობა:", find_maximum(numbers))

def my_function():
    # კოდის ბლოკი
    print("Hello, World!")
