frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [5, 6, 'c']]
print(matriz[0][0])
print(matriz[-1][-1])

lista = list('python')
print(lista[2:])
print(lista[:2])
print(lista[1:4:2])
print(lista[:])
print(lista[::-1])

carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1,  30, 21, 2, 9, 65, 34]
pares = [n for n in numeros if n % 2 == 0]
quadrado = [n**2 for n in numeros]
print(pares)
print(quadrado)

numeros = [1,  30, 21, 2, 9, 65, 34]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)