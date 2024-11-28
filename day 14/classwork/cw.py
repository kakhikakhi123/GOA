us = input("შეიყვანეთ რიცხვი: ")
num = int(us)

if num < 100:
    print(num, "ნაკლებია 100-ზე.")
else:
    print(num, "არ არის ნაკლები 100-ზე.")

if num > 50:
    print(num, "მეტია 50-ზე.")
else:
    print(num, "არ არის მეტია 50-ზე.")

if num == 25:
    print(num, "ტოლია 25-ის.")
else:
    print(num, "არ არის ტოლი 25-ის.")
