def generate_massiv(nazv):
    size = (int(input("Введите размер массива " + nazv + " ")))
    massiv = []
    for i in range(0,size):
        massiv.append((input("Введите следующее число массива " + nazv + " " )))
    return massiv
massiv_A = generate_massiv("A")
massiv_B = generate_massiv("B")
ans = list(set(massiv_A).intersection(massiv_B))
print(ans)
        

    
