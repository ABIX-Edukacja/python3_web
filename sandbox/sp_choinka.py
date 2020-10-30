# pętla, za pomocą której "rysujemy"
for i in range(5):
    print( i * " ", end="")
    print((9-2*i) * "@")

print("")
print("=" * 9)
print("")

for i in range(5):
    linia = "#" * (9 - 2*i)
    print(linia.center(9))
