# Python 3 - by Adam Jurkiewicz
# definiujemy funkcję, która zwraca dane
# po obliczeniu pewnych zależności

def value(some_number):
    if some_number > 0:
        returned_value = some_number * 4 - 5
    else:
        returned_value = some_number * 3 + 50

    return returned_value

# dla różnych wartości w liście obliczamy wyniki

numbers = [-15, -11, -6, -4, -1, 0, 1, 5, 8, 13, 16]

print(f"We will compute for: {numbers}")
print("---------------------")
for number in numbers:
    new_value = value(number)
    print(f"For {number} value is: {new_value}")
