# mamy 3 prostokąty, podajemy ich wymiary, liczymy powierchnie

def prost():
    a = float(input("podaj bok a: "))
    b = float(input("podaj bok b: "))
    pole = a*b
    obwod = 2*(a+b)
    print(f"Pole to {pole}, obwód = {obwod}")

prost()
print("==============================")
prost()