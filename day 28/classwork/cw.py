# creating a list with 5 elements
my_list = ["მაშინ", "რომ", "გგგ", "გეც", "ხხხ"]

# printing each element using its index
print(my_list[0])  # "მაშინ"
print(my_list[1])  # "რომ"
print(my_list[2])  # "გგგ"
print(my_list[3])  # "გეც"
print(my_list[4])  # "ხხხ"

# შექმენით სია სამი რიცხვით
my_list = [5, 10, 15]

# შეცვალეთ მენულე ინდექსზე მყოფი რიცხვი, გაზარდეთ ის ათით
my_list[1] = my_list[1] + 10

# დაბეჭდეთ პირველი და მესამე რიცხვების ჯამი
result = my_list[0] + my_list[2]
print(result)

# მომხმარებლისგან რიცხვის მიღება
number = int(input("შეიყვანეთ რიცხვი: "))

# სიის შექმნა 10 ელემენტით
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# თუ რიცხვი აღემატება სიის ინდექსების რაოდენობას, გამოვიტანთ შეცდომას
if 0 <= number < len(my_list):
    print(f"სიის {number}-ე ინდექსზე მყოფი ელემენტი არის: {my_list[number]}")
else:
    print("შევიყვანეთ სწორი ინდექსი!")
