massiv = list(map(float,input("Введите массив через пробел ").split()))
minimum = min(massiv)
delta = float(input("Введите дельту "))
print(massiv.count(delta + minimum))