# Python 3 - by Adam Jurkiewicz
# definiujemy listę, a więc kolekcję
# lista zawiera nazwiska i imiona znajomych
# za pomocą pętli iteracyjnej for wypisujemy kolejne pozycje
# i sprawdzamy płeć osoby

contacts = ["Jurkiewicz Adam", "Jurkiewicz Roman",
            "Jurkiewicz Beata", "Jurkiewicz Elżbieta",
            "Jurkiewicz Leon", "Jurkiewicz Henryka",
            ]

for contact in contacts:
    print(f"Person name is: {contact}")
    if contact.endswith("a"):
        print("Sounds like a woman...")
    else:
        print("Sounds like a men...")
