# ფუნქციის შექმნა
def square(user_num):
    return user_num * user_num

# ფუნქციის გამოძახება და დაბრუნებული მნიშვნელობის შენახვა ცვლადში
result = square(5)

# ცვლადის მნიშვნელობის გამრავლება ორზე და დაბეჭდვა
print(result * 2)

# ფუნქციის შექმნა
def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst

# ფუნქციის გამოძახება და სიიდან ელემენტის ამოშლა
my_list = [10, 20, 30, 40, 50]
index_to_remove = 2
updated_list = remove_one_element(my_list, index_to_remove)

# სიიდან ამოშლილი ელემენტის შედეგად ჩამოყალიბებული სიიდან დაბეჭდვა
print(updated_list)

def rectangle_info(side1, side2):
    perimeter = (side1 + side2) * 2
    area = side1 * side2
    return perimeter, area

# გამოიყენეთ ფუნქცია
side1 = 5
side2 = 10
perimeter, area = rectangle_info(side1, side2)

# ბეჭდვა შედეგის
print("Perimeter:", perimeter)
print("Area:", area)
