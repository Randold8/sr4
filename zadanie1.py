size = int(input("Введите размер массива "))
massiv = []
for i in range(0,size):
    massiv.append(float(input("Введите следующее число массива " )))
    if massiv[i].is_integer():
        massiv[i] = int(massiv[i])
max_value = max(massiv)
max_index = massiv.index(max_value)
for i in range(max_index + 1,size):
    massiv[i] = 0
print(massiv)