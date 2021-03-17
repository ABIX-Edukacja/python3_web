# test dla szkoły ponadpodstawowej

def test(liczba: int) -> bool:
    if type(liczba) is not int:
        return False

    wynik = False
    # tutaj Twój blok kodu

    return wynik

print(test(3.14)) # False
print(test("Ala")) # False
print(test(3)) # False
print(test(4)) # True


