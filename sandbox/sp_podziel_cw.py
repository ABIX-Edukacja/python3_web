# zapisz program sprawdzający podzielność liczb


def test_podzielnosci(liczba):
    """liczba : int"""
    if type(liczba) is not int:
        return False
    # tutaj lista liczb, przez które możemy podzielić od 2 .. 9
    liczby = []
    # tu sprawdź podzielność dla kolejnych liczb
    # i dodaj je do listy liczby
    # ... tu wypełnij swój kod
    #
    return liczby


# testy
print("False ->", test_podzielnosci("Nic"))
print("False ->", test_podzielnosci(3.14))
print("[3] ->", test_podzielnosci(33))
print("[2,3,6,9] ->", test_podzielnosci(18))
