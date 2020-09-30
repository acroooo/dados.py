# -*- coding: utf-8 -*-
from random import randint

def dados():
    """Este programa elegirá dos números aleatorios entre 1 y 6.
    el programa los imprime en pantalla, imprime su suma y pregunta
    al usuario si quiere tirar los dados otra vez"""
    decision = input("¿Desea jugar con dados? (responder s/n): ")
    while decision in 'n':
        break
    while decision in 's':
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        suma = dado1 + dado2
        print(f"El primer dado es {dado1}, el segundo es {dado2} y la suma de estos es {suma}")
        seguir = input("¿Desea volver a jugar? : ")
        if seguir in 's':
            continue
        else:
            print('Hasta luego')
            break

print(dados())