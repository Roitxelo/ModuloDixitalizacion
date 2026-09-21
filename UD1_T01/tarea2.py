listaNum = list(map(int, input("Escribe un lista números separados por espacios.").split(" ")))

pares = [n for n in listaNum if n%2==0]
impares = [n for n in listaNum if n%2!=0]

print(f"Pares: {pares}")
print(f"Impares: {impares}")