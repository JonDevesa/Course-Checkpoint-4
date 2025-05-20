print('Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.')
cool_list = ["Gustave", "Maelle", "Lune", "Sciel"]
print("List:", cool_list)
cool_tuple = ("sword and dagger", "rapier", "magic", "double scythe")
print("Tuple:", cool_tuple)
cool_float = 3.14
print("Float:", cool_float)
cool_integer = 42
print("Integer:", cool_integer)
from decimal import Decimal
cool_decimal = Decimal("10.75")
print("Decimal:", cool_decimal)
cool_dictionary = {
    "name": "Jon",
    "age": 33,
    "likes": "Gaming"
}
print("Dictionay:", cool_dictionary)
print()

print('Exercise 2: Round your float up.')
import math
round_up_float = math.ceil(cool_float)
print("Rounded up float:", round_up_float)
print()

print('Exercise 3: Get the square root of your float.')
square_root_float = math.sqrt(cool_float)
print("Square root of float:", square_root_float)
print()

print('Exercise 4: Select the first element from your dictionary.')
first_key = list(cool_dictionary.keys())[0]
first_value = list(cool_dictionary.values())[0]
print("First element, key-value pair, from my dictionary:", f"{first_key}: {first_value}")
print()

print('Exercise 5: Select the second element of your tuple.')
second_element = cool_tuple[1]
print("Second element:", second_element)
print()

print('Exercise 6: Add an element to the end of your list.')
cool_list.append("Monoco")
print("List with new element:", cool_list)
print()

print('Exercise 7: Replace the first element in your list.')
cool_list[0] = "Verso"
print("List with replaced element:", cool_list)
print()

print('Exercise 8: Sort your list alphabetically.')
cool_list.sort()
print("Sorted list:", cool_list)
print()

print('Exercise 9: Use reassignment to add an element to your tuple.')
cool_tuple = cool_tuple + ("staff",)
print("Tuple with new element:", cool_tuple)
print()