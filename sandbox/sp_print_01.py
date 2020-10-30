# podstawowe polecenie - wypisywanie na ekran
print("Nasz tekst, który chcemy wypisać.")
print("Musi znajdować się w cudzysłowach.")
print('Mogą być podwójne, jak: "')
print("Lub pojedyncze, jak: '")
print("Możemy", "pisać", "kilka", "elementów", "z przecinkami.")

# wypisywanie zawartości zmiennych
zmienna_a = 102
pi = 3.14
promien = 25
pole_kola = pi * promien**2

print("Koło o promieniu", promien, "ma pole", pole_kola)
# lub to samo w wersji f-string
print(f"Koło o promieniu {promien} ma pole {pole_kola}")
# działanie paramtetru sep
print("Koło o promieniu", promien, "ma pole", pole_kola, sep="+++")
# działanie parametru end
print("Koło o promieniu", promien, "ma pole", pole_kola, end="****")
print("")
# dziaałanie sep i end jednocześnie
print("Koło o promieniu", promien, "ma pole", pole_kola, sep="+++", end="****")
