# 2) Tuple Indexing & Slicing
my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_slice = my_tuple[1:4]
print("Second element:", second_element)
print("Last element:", last_element)
print("Middle three elements:", middle_slice)

# 3) Tuple Immutability
my_tuple = (10, 20, 30)
try:
    my_tuple[1] = 99  # Attempt to modify
except TypeError as e:
    print("Error:", e)

# 4) Tuple Packing & Unpacking
packed_tuple = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = packed_tuple
print("Fruit 1:", fruit1)
print("Fruit 2:", fruit2)
print("Fruit 3:", fruit3)

# 5) Tuple Methods
my_tuple = (1, 2, 3, 2, 2, 4)
count_of_twos = my_tuple.count(2)
index_of_three = my_tuple.index(3)
print("Count of 2s:", count_of_twos)
print("Index of first occurrence of 3:", index_of_three)

# 6) Set Creation & Basic Operations
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
is_four_present = 4 in my_set
print("Updated Set:", my_set)
print("Is 4 present in the set?", is_four_present)

# 7) Removing Duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
unique_list = list(unique_set)
print("Original list:", my_list)
print("List without duplicates:", unique_list)
