#!/usr/bin/python3
# Coding: utf-8
# !! By AloNE - Legends Company

print("  ____ ___  ____ _____  ____")
print(" / ___/ _ \|  _ \___ / / ___|")
print("| |  | | | | | | ||_ \| |")
print("| |__| |_| | |_| |__) | |___")
print(" \____\___/|____/____/ \____| 1.3")

print("\nSeleccione el cifrado deseado:\n")

print("1- Atbash   2- Decrypt")
print("3- Cesar    4- BruteForce - Decrypt")

select = int(input("\nIngrese el número del cifrado: "))

# Atbash Encrypt
if select == (1):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifra = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    mensaje = input("Ingrese el texto a cifrar: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    mensaje_cifrado = ""

    for letra in mensaje.lower():

        if letra in alfabeto:
            posicion = alfabeto.index(letra)
            letra_cifrada = cifra[posicion]
            mensaje_cifrado += letra_cifrada

        else:
            mensaje_cifrado += letra
    
    print("Cifrado: ATBASH")
    print("Mensaje Plano: {}".format(mensaje))
    print("[*] Mensaje Cifrado: {}\n".format(mensaje_cifrado))

# Atbash Decrypt
if select == (2):
    alfabeto_cifrado = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    alfabeto_plano = "abcdefghijklmnopqrstuvwxyz"
    
    mensaje_cifrado = input("\nIngrese el texto a descifrar: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    mensaje_plano = ""

    for letra in mensaje_cifrado.upper():
        if letra in alfabeto_cifrado:
            posicion = alfabeto_cifrado.index(letra)
            letra_plana = alfabeto_plano[posicion]
            mensaje_plano += letra_plana

        else:
            mensaje_plano += letra

    print("Cifrado: ATBASH")
    print("Mensaje Cifrado: {}".format(mensaje_cifrado))
    print("[*] Mensaje Plano: {}\n".format(mensaje_plano))

# Cesar Encrypt
if select == (3):
    alfabeto_cifrado = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    mensaje = input("Ingrese el texto a cifrar: ")
    mensaje_cifrado = ""

    clave = int(input("Introduce la clave deseada: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for letra in mensaje.upper():

        if letra in alfabeto_cifrado:
            posicion = alfabeto_cifrado.index(letra)
            posicion = (posicion + clave) % len(alfabeto_cifrado)
            mensaje_cifrado += alfabeto_cifrado[posicion]

        else:
            mensaje_cifrado += letra

    print("Cifrado: Cesar")
    print("Mensaje Plano: {}".format(mensaje))
    print("[*] Mensaje Cifrado: {}\n".format(mensaje_cifrado))

# Cesar Decrypt - Brute Force
if select == (4):
    alfabeto_cifrado = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    mensaje_cifrado = input("Ingrese el texto a descifrar: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    mensaje_plano = ""

    for clave in range(1, len(alfabeto_cifrado)):

        mensaje_plano = ""

        for letra in mensaje_cifrado:
            posicion = alfabeto_cifrado.index(letra)
            posicion = (posicion - clave) % len(alfabeto_cifrado)
            mensaje_plano += alfabeto_cifrado[posicion]

        else:
            mensaje_plano += letra

        print("[*] Clave {}: {}".format(clave, mensaje_plano))
