# შეინახეთ სწორი რიცხვი
correct_num = 10

# უსასრულო ციკლი, რათა მუდმივად ითხოვდეს მომხმარებლისგან რიცხვის შეყვანას
while True:
    # მომხმარებლისგან მთელი რიცხვის მიღება
    user_guess = int(input("შეიყვანეთ მთელი რიცხვი: "))

    # შეამოწმეთ, არის თუ არა მომხმარებლის რიცხვი სწორი
    if user_guess == correct_num:
        print("correct guess")  # თუ სწორი, გამოუშვით შეტყობინება
        break  # დაასრულეთ ციკლი
    else:
        print("ცუდი გესია, სცადეთ ისევ.")  # თუ არასწორია, კვლავ სთხოვეთ მომხმარებელს
