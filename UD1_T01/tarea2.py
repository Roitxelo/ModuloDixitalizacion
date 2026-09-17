listaNum = input(print("Escribe un lista números separados por espacios."))

arrayPares, arrayImpares = array('i')
cPares, cImpares = 0
arrayNum = listaNum.split(" ")

for num in arrayNum:
    if num % 2 == 0:
        arrayPares[cPares] = num
        cPares + 1
    else:
        arrayImpares[cImpares] = num
        cImpares + 1
        