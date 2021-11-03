# Python 3 - by Adam Jurkiewicz
# Za pomocą input() wczytujemy wartość, zmieniamy typ i obliczmy wiek
# skrypt z instrukcjami warunkowymi i blokami kodu

actual_year = 2021

print("Hi, we'll try to compute your age ;-)")
name = input("Please tell me your name:")
birth = input(f"OK {name} - at what year have you birth?")
print(f"Now birth is a {type(birth)}")
# Uwaga - poniżej następuje zmiana typu na int - liczbę całkowitą !!!!!!
birth = int(birth)
print(f"Now birth is a {type(birth)} - after using int() function.")
age = actual_year - birth

if age >= 18:
    print(f"Oh, I see, {name} - you are an adult now.")
    print(f"You are {age} years old.")
else:
    print(f"You are young - {age} years old.")

print("That is all - see you next time!")
