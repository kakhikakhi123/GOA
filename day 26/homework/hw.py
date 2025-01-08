# Taking three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Comparing the numbers and finding the largest one
largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Printing the largest number
print("The largest number is:", largest)

# Define the correct password
correct_password = "Goa best"

# Initialize the incorrect password attempt counter
incorrect_count = 0

# Start the while loop to ask for the password
while True:
    # Ask the user to input a password
    user_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if user_password == correct_password:
        print("Password correct!")
        break  # Exit the loop when the correct password is entered
    else:
        incorrect_count += 1  # Increment the counter for incorrect passwords
        print("Incorrect password. Try again.")

# Print the count of incorrect password attempts
print(f"Incorrect password attempts: {incorrect_count}")

# Take two numbers and an operator as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Display the result
print("Result:", result)
