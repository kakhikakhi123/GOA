# მიღება მთელ რიცხვს
number = int(input("შეიყვანეთ მთელი რიცხვი: "))

# პირობითი განცხადება
if number > 0:
    print("Bigger than 0")
elif number == 0:
    print("0")
else:
    print("smaller than 0")
 
 # პირველი და მეორე რიცხვების შეყვანა
first_number = int(input("შეიყვანეთ პირველი რიცხვი: "))
second_number = int(input("შეიყვანეთ მეორე რიცხვი: "))

# შეამოწმეთ რიცხვების შედარება
if first_number > second_number:
    # თუ პირველი რიცხვი მეტია მეორეზე, შექმენით დიაპაზონი მეორე რიცხვისგან პირველ რიცხვამდე
    for num in range(second_number, first_number + 1):
        print(num)
elif second_number > first_number:
    # თუ მეორე რიცხვი მეტია პირველზე, შექმენით დიაპაზონი პირველ რიცხვისგან მეორე რიცხვამდე
    for num in range(first_number, second_number + 1):
        print(num)
else:
    # როდესაც რიცხვები ტოლია
    print("numbers are equal")

# Input: Score (0-100)
score = int(input("Enter the score (0-100): "))

# Determine the grade based on the score
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Output: Grade
print(f"The grade is: {grade}")
