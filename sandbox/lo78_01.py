# Python 3 - by Adam Jurkiewicz
print("To jest pierwsza linia.")

# komentarz - nic nie wnosi, poza informacjami
# definiujemy zmienne różnego typu

language = "Python"     # str   - ciąg znaków
year_of_birth = 1991    # int   - liczba całkowita
version = 3.8           # float - liczba rzeczywista, zmiennoprzecinkowa
is_cool = True          # bool  - wartość logiczna (prawda/fałsz)

pi = 3.1415927
circle_radius = 6
print("Hi, I want to compute some things!")
circle_area = pi * circle_radius ** 2

# wypisujemy na ekranie stosując konwencję F-String
print(f"Area is {circle_area}")

# wypisujemy informacje o typie danych:
print(f"Typ zmiennej language to {type(language)}.")
print(f"Typ zmiennej year_of_birth to {type(year_of_birth)}.")
print(f"Typ zmiennej version to {type(version)}.")
print(f"Typ zmiennej is_cool to {type(is_cool)}.")
print(f"Typ zmiennej circle_area to {type(circle_area)}.")
