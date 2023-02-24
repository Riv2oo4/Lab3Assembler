def hexa():
    hex_num = input("Ingrese un número de 3 dígitos en hexadecimal: ")
    dec_num = 0
    for i in range(len(hex_num)):
        dec_num += int(hex_num[i], 16) * 16 ** (len(hex_num) - i - 1)
    print("El número hexadecimal {} en decimal es: {}".format(hex_num, dec_num))

def decimal():
    dec_num = int(input("Ingrese un número decimal: "))
    hex_num = ""
    while dec_num > 0:
        rem = dec_num % 16
        if rem < 10:
            hex_num += str(rem)
        else:
            hex_num += chr(ord('A') + rem - 10)
        dec_num //= 16
    hex_num = hex_num[::-1]
    print("El número decimal {} en hexadecimal es: {}".format(dec_num, hex_num))


numero = int(input('Hexadecimal -> decimal (1) \nDecimal -> Hexadecimal (2) \nSalir(3)\n'))
while numero != 3:
    if numero == 1:
        hexa()
    if numero == 2:
        decimal()

    numero = int(input('Hexadecimal -> decimal (1) \nDecimal -> Hexadecimal (2) \nSalir(3)\n'))

