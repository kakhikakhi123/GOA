# მომხმარებლისგან რიცხვის მიღება
number = int(input("შეიყვანეთ რიცხვი: "))

# პირობა, თუ რიცხვი მეტია 10-ზე ან ნაკლები
if number > 10:
    print("bigger than 10")
else:
    print("smaller than 10")

# მომხმარებლისგან "yes"-ის ან "Yes"-ის მიღება
response = input("Are you a student? (yes/Yes): ")

# პირობა, თუ პასუხი "yes" ან "Yes"
if response == "yes" or response == "Yes":
    is_student = True
else:
    is_student = False

# ცვლადის გაჩენა
print("is_student =", is_student)

