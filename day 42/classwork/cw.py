def find_max_with_max_function(numbers):
    # Finding the maximum number using the max() function
    return max(numbers)

def find_max_with_loop(numbers):
    # Finding the maximum number using a loop
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def sum_of_squares_of_positives(numbers):
    # Calculating the sum of squares of positive numbers
    return sum(num**2 for num in numbers if num > 0)

# Example list of numbers
numbers = [-4, 7, -2, 10, 3]

# Using the max() function
print("Maximum using max():", find_max_with_max_function(numbers))  # Output: 10

# Using a loop
print("Maximum using loop:", find_max_with_loop(numbers))  # Output: 10

# Sum of squares of positive numbers
print("Sum of squares of positives:", sum_of_squares_of_positives(numbers))  # Output: 158
