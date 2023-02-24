def a1():
    binario = input("Ingrese un número binario de 8 bits: ")
    complemento1 = ""
    for bit in binario:
        complemento1 += "0" if bit == "1" else "1"
    print("El complemento a 1 es:", complemento1)


def a2():
    binario = input("Ingrese un número binario de 8 bits: ")
    num = 0
    for i in range(8):
        num += int(binario[i]) * 2**(7-i)
    complemento1 = 255 - num
    complemento2 = complemento1 + 1
    print("El complemento a 2 es:", '{0:08b}'.format(complemento2))


numero = int(input('Binario -> a 1 (1) \nBinario -> a 2 (2) \nSalir(3)\n'))
while numero != 3:
    if numero == 1:
        a1()
    if numero == 2:
        a2()

    numero = int(input('Binario -> a 1 (1) \nBinario -> a 2 (2) \nSalir(3)\n'))