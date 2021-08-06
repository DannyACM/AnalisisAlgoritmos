val = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
peso = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
capacidad = 140

nItems = len(val)
tabla =[[ i for i in range (capacidad + 1)] for x in range(nItems+ 1)]
for i in range(nItems + 1):
    for j in range(capacidad + 1):
        if i == 0 or j == 0:
            tabla[i][j] = 0
        elif peso[i-1] <= j:
            tabla [i][j] = max(val[i-1] + tabla[i-1][j-peso[i-1]],  tabla[i-1][j])


print(tabla[nItems][capacidad])

