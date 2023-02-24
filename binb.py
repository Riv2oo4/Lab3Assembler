def a1():
    binario = input("Ingrese un número binario de 8 bits: ")
    complemento1 = ""
    for bit in binario:
        complemento1 += "0" if bit == "1" else "1"
    print("El complemento a 1 es:", complemento1)


def a2():
    binario = input("Ingrese un número binario de 8 bits: ")
    complemento2 = ""
    carry = 1
    for bit in binario[::-1]:
        suma = int(bit) + carry
        complemento2 = str(suma % 2) + complemento2
        carry = 1 if suma > 1 else 0
    print("El complemento a 2 es:", complemento2)


numero = int(input('Binario -> a 1 (1) \nBinario -> a 2 (2) \nSalir(3)\n'))
while numero != 3:
    if numero == 1:
        a1()
    if numero == 2:
        a2()

    numero = int(input('Binario -> a 1 (1) \nBinario -> a 2 (2) \nSalir(3)\n'))