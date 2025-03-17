# 2) Function Basics: Write a function that takes no arguments and simply prints "Hello, World!"
def print_hello():
    print("Hello, World!")
# Call the function
print_hello()

# 3) Arguments and Parameters: Write a function that takes two numbers as arguments and prints their sum.
def print_sum(a, b):
    print("The sum is:", a + b)
# Example call
print_sum(5, 10)

# 4) Return Statement: Create a function that takes a number as input, multiplies it by 10, and returns the result.
def multiply_by_ten(number):
    return number * 10
# Example call
result = multiply_by_ten(7)
print("Result is:", result)

# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.
def greet(name="Guest"):
    print("Hello,", name)
# Example calls
greet("Kaxi")
greet()

# 6) Boss Level: Nested Functions: Define a function that contains another function inside it and calls the inner function.
def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    print("Calling the inner function...")
    inner_function()
# Example call
outer_function()

# 7) Check Even or Odd: Write a function that takes a list of numbers and checks whether each number is even or odd.
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
# Example call
check_even_odd([1, 2, 3, 4, 5])

# 8) Find the Maximum: Create a function that takes a list of numbers and finds the maximum.
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
# Example call
print("Maximum is:", find_maximum([10, 25, 7, 99, 4]))

# 9) Positive Numbers: Define a function that takes a list of integers and returns only the positive ones.
def get_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers
# Example call
print("Positive numbers:", get_positive_numbers([-5, 0, 6, 10, -3, 8]))

# 10) Sum Divisible by 3: Write a function that sums up all numbers divisible by 3 in a range.
def sum_divisible_by_3(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total_sum += num
    return total_sum
# Example call
print("Total sum:", sum_divisible_by_3(1, 100))
