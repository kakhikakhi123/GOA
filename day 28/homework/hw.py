# Create a list of five numbers
numbers = [10, 20, 30, 40, 50]

# Print the first, third, and last elements using positive indexing
print("First element:", numbers[0])   # First element (index 0)
print("Third element:", numbers[2])   # Third element (index 2)
print("Last element:", numbers[4])    # Last element (index 4)

# Create a list of 20 elements with different data types
elements = [10, 'hello', 3.14, True, [1, 2, 3], {'key': 'value'}, None, 45, 50.5, 'world', False, (4, 5), 'python', 99, 101, 200, {'a': 1}, ['a', 'b', 'c'], 12.34, 'test', 7]

# Print all of the elements using indexing
for i in range(len(elements)):
    print(elements[i])

# List of five numbers
numbers = [10, 20, 30, 40, 50]

# Printing the first, third, and last elements using negative indexing
print(numbers[-5])  # First element
print(numbers[-3])  # Third element
print(numbers[-1])  # Last element

# Ask the user for their name
name = input("Please enter your name: ")

# Get the first and last symbols using indexing
first_symbol = name[0]
last_symbol = name[-1]

# Print the first and last symbols
print("First symbol:", first_symbol)
print("Last symbol:", last_symbol)

