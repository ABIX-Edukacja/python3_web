# wykonujemy pętlę
for e in range(5):
    # wewnątrz pętli stosujemy instrukcję warunkową
    if e % 2 == 0:
        # liczba parzysta
        print("* ? * ? *")
    else:
        # w innym przypadku
        print("? * ? * ?")

#
print("------[ Inna wersja: Marcinosoft Mst]-------")
print("".join("?*"[x % 2 - 1] + " " + "\n" * (x % 5 - 3) for x in range(25)))

#
print("------[ Inna wersja: Janek Barański ]-------")
print("\n".join([" ".join(s[:5]) for s in ["*?" * 3, "?*" * 3] * 3][:5]))
